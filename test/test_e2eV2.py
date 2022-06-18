# End to end testing using pytest framework V2
# Cleaner version, no comments.
# Optimized with methods from BaseClass and using Page objects optimization
from Utilities.BaseClass import BaseClass
from pageObjects.Homepage import HomePage
import pytest
class TestOne(BaseClass):

    def test_e2e(self):
        # Lets call the logger method at the beginning of the test
        log = self.getLogger()
        homepage = HomePage(self.remotedriver)
        checkoutpage = homepage.shopItem()
        log.info("getting all the products titles")
        products = checkoutpage.getproduct()
        i = -1
        for product in products:
            i = i+1
            productText = product.text
            log.info(productText)
            if productText == "Blackberry":
                checkoutpage.getproductButton()[i].click()

        checkoutpage.getproductCheckoutBlue().click()
        confirmpage = checkoutpage.getproductCheckoutGreen()
        log.info("Entering country name as ind")
        confirmpage.getinputCountry().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmpage.getconfirmCountry().click()
        confirmpage.getcheckbox().click()
        #self.remotedriver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        # Press purchase
        confirmpage.getconfirmPurchase().click()
        #self.remotedriver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        # Assert that success msg is pass
        msg = confirmpage.getconfirmMsg().text
        #msg = self.remotedriver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        log.info("Text received from application is "+msg)
        assert "Success! Thank you!" in msg
        # Lets save a screenshot
        # Usually you get screenshot when something fails
        #self.remotedriver.get_screenshot_as_file("screen.png")