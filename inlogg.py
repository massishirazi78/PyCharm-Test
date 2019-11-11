from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

from WebShopG3.pages.homePage import HomeP
from WebShopG3.pages.loginPage import logP

# import HtmlTestRunner


class logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(
            executable_path="C:/Users/sofia/PycharmProjects/FirstSeleniumTest/driver/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")


        login = logP(driver)
        login.enter_username("massi.shirazi2018@outlook.com")
        login.enter_password("massi12345")
        login.click_login()

        homepage = HomeP(driver)
        homepage.click_welcom()
        homepage.click_logout()

        time.sleep(2)

    def test_02_login_invalid_username(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")

        login = logP(driver)
        login.enter_username("massi@outlook.com")
        login.enter_password("massi12345")
        login.click_login()
        message = driver.find_element_by_xpath("/html/body/div").text
        self.assertEqual(message, "Fel email eller lösenord!")
        time.sleep(2)

    def test_03_login_invalid_password(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")

        login = logP(driver)
        login.enter_username("massi.shirazi2018@outlook.com")
        login.enter_password("massi45")
        login.click_login()
        message = driver.find_element_by_xpath("/html/body/div").text
        self.assertEqual(message, "Fel email eller lösenord!")
        time.sleep(2)

    def test_04_login_invalid_UsPas_longString(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")

        login = logP(driver)
        login.enter_username("665765jhbhhjhhhf@outlnnnnnnnnnkkkkkkkkkkkkkkkkkkoonbbk.com")
        login.enter_password("vhvvvvvvvvvvvhgvuyoiuoipåobjvs<<zdfvhgrerrvyrmmmmmmmmmmmmmmmmmmmmmmmmmmmmxrfg ")
        login.click_login()
        message = driver.find_element_by_xpath("/html/body/div").text
        self.assertEqual(message, "Nu skrev du nog för mycket.")
        time.sleep(2)

    def test_05_login_invalid_password_ChinaLa(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")

        login = logP(driver)
        login.enter_username("massi.shirazi2018@outlook.com")
        login.enter_password("华语华语华语华语")
        login.click_login()
        message = driver.find_element_by_xpath("/html/body/div").text
        self.assertEqual(message, "Nu skrev du nog för mycket.")
        time.sleep(2)

    def test_06_login_invalid_password_Farsi(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")

        login = logP(driver)
        login.enter_username("massi.shirazi2018@outlook.com")
        login.enter_password("گکثابابخحصحبدم")
        login.click_login()
        message = driver.find_element_by_xpath("/html/body/div").text
        self.assertEqual(message, "Nu skrev du nog för mycket.")
        time.sleep(2)

    def test_07_login_invalid_password_longText(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")

        login = logP(driver)
        login.enter_username("massi.shirazi2018@outlook.com")
        login.enter_password(
            "En text som ska läsas på skärm måste skrivas på ett annat sätt än en text som ska läsas på papper. Det är lätt att inse om man tänker på de olika lässituationerna. Du vet redan från början om en text på papper är på tre eller på femton sidor. Det är inte lika uppenbart när du läser på skärm.")
        login.click_login()
        message = driver.find_element_by_xpath("/html/body/div").text
        self.assertEqual(message, "Nu skrev du nog för mycket.")
        time.sleep(2)

    def test_08_login_invalid_password_htmlkod(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")

        login = logP(driver)
        login.enter_username("massi.shirazi2018@outlook.com")
        login.enter_password("h1 {color: white;  text-align: center;}")
        login.click_login()
        message = driver.find_element_by_xpath("/html/body/div").text
        self.assertEqual(message, "Nu skrev du nog för mycket.")
        time.sleep(2)

    def test_09_login_invalid_password_emoji(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")

        login = logP(driver)
        login.enter_username("massi.shirazi2018@outlook.com")
        login.enter_password("😥 😮 🤐 😯 😪 😫 😴")
        login.click_login()
        message = driver.find_element_by_xpath("/html/body/div").text
        self.assertEqual(message, "Nu skrev du nog för mycket.")
        time.sleep(2)

    def test_10_login_invalid_password_spaceAfter(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")

        login = logP(driver)
        login.enter_username("massi.shirazi2018@outlook.com")
        login.enter_password("massi12345  ")
        login.click_login()

        message = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/a").text
        self.assertEqual(message, "Lägg i varukorg")
        time.sleep(2)

    def test_11_login_invalid_password_spaceBefor(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")

        login = logP(driver)
        login.enter_username("massi.shirazi2018@outlook.com")
        login.enter_password("  massi12345")
        login.click_login()

        message = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/a").text
        self.assertEqual(message, "Lägg i varukorg")
        time.sleep(2)

    def test_12_login_invalid_password_spaceBetween(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")

        login = logP(driver)
        login.enter_username("massi.shirazi2018@outlook.com")
        login.enter_password("massi  12345")
        login.click_login()

        message = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/a").text
        self.assertEqual(message, "Lägg i varukorg")
        time.sleep(2)

    def test_13_login_invalid_password_space(self):
        driver = self.driver
        driver.get("http://jbjork.nu/login.php")

        login = logP(driver)
        login.enter_username("massi.shirazi2018@outlook.com")
        login.enter_password("  massi  12345  ")
        login.click_login()

        message = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/a").text
        self.assertEqual(message, "Lägg i varukorg")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest.main()
#        testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/sofia/PycharmProjects/FirstSeleniumTest/Report'))

# cd C:\Users\sofia\PycharmProjects\FirstSeleniumTest
# python -m WebShopG3.test.inlogg
