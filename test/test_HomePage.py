# Test for only homepage
# Separate the test by webpage
from selenium.webdriver.support.select import Select

from Utilities.BaseClass import BaseClass
from pageObjects.Homepage import HomePage
from TestData.HomePageData import HomePageData
import pytest


class TestHomePage(BaseClass):

    def test_homepage(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.remotedriver)
        log.info("First Name is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        log.info("Email is " + getData["email"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getId().click()
        log.info("Gender is " + getData["gender"])
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.getSubmit().click()
        alertText = homepage.getAlert().text

        assert ("Success" in alertText)
        # This will refresh and clear the current data, usefull if you multiple sets of data
        self.remotedriver.refresh()

    # Instead of using hardcoded params lets try using the exel method
    #@pytest.fixture(params = HomePageData.test_HomePage_Data)
    @pytest.fixture(params=HomePageData.getTestData("Testcase1"))
    def getData(self, request):
        return request.param


