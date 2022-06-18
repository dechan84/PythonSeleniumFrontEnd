import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = None
# from selenium.webdriver.firefox.service import Service
# Parsing switches to the python cmd line
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default = "chrome"
    )

@pytest.fixture(scope ="class")
# Use request to use the driver object without the need to use return
def setup(request):
    # Request to use global driver, not the one declared in setup
    global driver
    # This cmd request.config.getOption will extract the value from parser.addoption declared before
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        s = Service(executable_path=ChromeDriverManager().install())
        #s = Service("C:\\Users\\victo\\Documents\\Browsers\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    elif browser_name == "firefox":
        s = Service("C:\\Users\\victo\\Documents\\Browsers\\geckodriver-v0.31.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(service=s)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    # request.cls.driver means that we are sending our local object driver to the class that is requesting
    # it as object driver, by the way driver is just a variable name they dont need to be the same name
    # Now you dont need to return anything
    request.cls.remotedriver = driver
    # Remember to add yield for any action you want to occur after test finish
    # We cant use return driver before yield using driver command or it will fail
    yield
    driver.close()

# This method will get do 'something' whenever test fails, in this example we capture screenshot into html report
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
