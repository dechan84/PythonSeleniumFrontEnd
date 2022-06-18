from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ConfirmPage():
    def __init__(self, driver):
        self.driver = driver

    # This is how we catch all the objects we want
    inputCountry = (By.XPATH, "//input[@id='country']")
    waitCountry = (By.XPATH, "//a[normalize-space()='India']")
    confirmCountry = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//label[@for='checkbox2']")
    confirmPurchase = (By.XPATH, "//input[@value='Purchase']")
    confirmMsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def getinputCountry(self):
        return self.driver.find_element(*ConfirmPage.inputCountry)

    def getwaitCountry(self):
        return EC.presence_of_element_located(ConfirmPage.waitCountry)

    def getconfirmCountry(self):
        return self.driver.find_element(*ConfirmPage.confirmCountry)

    def getcheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getconfirmPurchase(self):
        return self.driver.find_element(*ConfirmPage.confirmPurchase)

    def getconfirmMsg(self):
        return self.driver.find_element(*ConfirmPage.confirmMsg)