import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.AddBasketPage import AddBasketPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Basket:
    baseURL = ReadConfig.getApplicationURL()

    # logger = LogGen.loggen()

    def test_basket(self, setup):
        # self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.lp = LoginPage(self.driver)
        self.lp.cookie_button()
        self.driver.maximize_window()
        time.sleep(3)
        self.abp = AddBasketPage(self.driver)
        self.abp.add_items()
        time.sleep(2)
        self.abp.click_subProduct()
        time.sleep(3)
        self.abp.add_toCart()
        time.sleep(3)
        self.abp.checkOut()
        time.sleep(3)
        self.abp.emptyBasket_button()
        time.sleep(3)


