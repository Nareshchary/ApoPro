import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.AddBasketPage import AddBasketPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.lp = LoginPage(self.driver)
        self.lp.cookie_button()
        time.sleep(3)
        self.lp.login_link()
        self.lp.setUserName(self.username)
        time.sleep(1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        act_title = self.driver.title
        if act_title == "Profil | Apopro.dk":
            self.logger.info("****Login test passed ****")

            #self.driver.save_screenshot(".\\Screenshots"+"test_login.png")
            assert True
        else:
            self.logger.error("****Login test failed ****")
            #self.driver.save_screenshot("test_login1.png")
            assert False

        self.lp.moveTo()
        time.sleep(3)

