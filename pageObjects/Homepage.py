from selenium.webdriver.common.by import By
# This is page object design, for each webpage we should create a class for all those objects
from pageObjects.Checkoutpage import CheckoutPage

class HomePage():
    # We need to create a constructor so we can receive the driver from the test
    def __init__(self, driver):
        self.driver = driver

    # This is how we catch all the objects we want
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    id = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    alert = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItem(self):
        # This command (with the *) will read variable shop as a tuple and serialize
        # it like this remotedriver.find_element(By.CSS_SELECTOR, "a[href*='shop']"), without * it will
        # just look like a normal tuple
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
        # return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getId(self):
        return self.driver.find_element(*HomePage.id)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)