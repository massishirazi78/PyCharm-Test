from selenium.webdriver.common.keys import Keys
from WebShopG3.Locators.locators import Locators


class logP():
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_Xpath = Locators.login_button_Xpath
        #self.invalid_username_message_xpath = "/html/body/div"

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_Xpath).send_keys(Keys.ENTER)

    def check_invalid_username_message(self):
        msg = self.driver.find_element_by_xpath("/html/body/div").text
        return msg
