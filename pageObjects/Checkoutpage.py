from selenium.webdriver.common.by import By
from pageObjects.Confirmpage import ConfirmPage


class CheckoutPage():
    # We need to create a constructor so we can receive the driver from the test
    def __init__(self, driver):
        self.driver = driver

    # This is how we catch all the objects we want
    productTitle = (By.CSS_SELECTOR, ".card-title a")
    productButton = (By.CSS_SELECTOR, ".card-footer button")
    productCheckoutBlue = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    productCheckoutGreen = (By.XPATH, "//button[normalize-space()='Checkout']")



    def getproduct(self):
        return self.driver.find_elements(*CheckoutPage.productTitle)

    def getproductButton(self):
        return self.driver.find_elements(*CheckoutPage.productButton)

    def getproductCheckoutBlue(self):
        return self.driver.find_element(*CheckoutPage.productCheckoutBlue)

    def getproductCheckoutGreen(self):
        self.driver.find_element(*CheckoutPage.productCheckoutGreen).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage