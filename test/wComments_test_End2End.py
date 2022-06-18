# End to end testing using pytest framework
# Replacing all Selenium python cmds with pytest Page objects mechanism
# We can also optimize the object creation for access in each webpage
# by moving the object creation in the method that is accessing the next webpage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from Utilities.BaseClass import BaseClass


# We invoke the parent class BaseClass to use the fixture, then we dont need to keep writing the usefixtures
# everytime
from pageObjects.Confirmpage import ConfirmPage
from pageObjects.Homepage import HomePage

class TestOne(BaseClass):

    def test_e2e(self):
        # Let's start an end 2 end test
        # Click Shop option using Page object
        # The next two cmds substitute #self.remotedriver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        homepage = HomePage(self.remotedriver)
        checkoutpage = homepage.shopItem()
        # homepage.shopItem().click()
        # Get the products list with page object in Checkoutpage
        # The next two lines replace
        # products = self.remotedriver.find_elements(By.XPATH, "//div[@class='card h-100']")
        # checkoutpage = CheckoutPage(self.remotedriver)
        # Instead of declaring the object of checkout page as shown above we added that in homepage.shopItem()
        products = checkoutpage.getproduct()

        i = -1
        for product in products:
            i = i+1
            productText = product.text
            print(productText)
            # productName = product.find_element(By.XPATH, "div/h4/a").text
            if productText == "Blackberry":
                # Add item into cart
                checkoutpage.getproductButton().click()
                # product.find_element(By.XPATH, "div/button").click()

        # Select checkout button

        checkoutpage.getproductCheckoutBlue().click()
        # checkoutpage.getproductCheckoutGreen().click()
        confirmpage = checkoutpage.getproductCheckoutGreen()
        # self.remotedriver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        # self.remotedriver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()

        # confirmpage = ConfirmPage(self.remotedriver)
        # Send country
        # confirmpage.inputCountry().send_keys("ind")
        confirmpage.getinputCountry().send_keys("ind")
        # self.remotedriver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
        # Wait for the autocomplete options
        # wait = WebDriverWait(self.remotedriver, 7)
        # wait.until(confirmpage.getwaitCountry())
        # wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='India']")))
        # This time the wait will be from a method in BaseClass
        self.verifyLinkPresence("India")
        confirmpage.getconfirmCountry().click()
        # self.remotedriver.find_element(By.LINK_TEXT, "India").click()
        # Check the terms and conditions
        confirmpage.getcheckbox().click()
        #self.remotedriver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        # Press purchase
        confirmpage.getconfirmPurchase().click()
        #self.remotedriver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        # Assert that success msg is pass
        msg = confirmpage.getconfirmMsg().text
        #msg = self.remotedriver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        print(msg)
        assert "Success! Thank you!" in msg
        # Lets save a screenshot
        # Usually you get screenshot when something fails
        #self.remotedriver.get_screenshot_as_file("screen.png")