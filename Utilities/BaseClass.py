import inspect
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# Invoke browser setup from fixture
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import logging

@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.remotedriver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    # Get logs info
    def getLogger(self):
        # This is to get the test name in another class
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        # addHandler uses filehandler object as parameter, now he will know the file name to print the log
        fileHandler = logging.FileHandler('logfile.log')
        # Select the format, in this case we use date and time (%(asctime)s), level of the log (%(levelname)s), testcase name
        # (%(name)s) and the message
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        # Setting log levels, this will filter some log messages and not display them all
        # Example will only print info level above messages (all debug msg will be ignored)
        logger.setLevel(logging.INFO)
        return logger


