from selenium.webdriver.common.keys import Keys
from WebShopG3.Locators.locators import Locators


class HomeP():
    def __init__(self, driver):
        self.driver = driver

        self.welcom_Xpath = Locators.welcom_Xpath
        self.logout_Xpath = Locators.logout_Xpath

    def click_welcom(self):
        self.driver.find_element_by_xpath(self.welcom_Xpath).send_keys(Keys.ENTER)

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_Xpath).send_keys(Keys.ENTER)
