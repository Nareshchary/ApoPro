from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class AddBasketPage:

    #select_product = "//a[@class='navtext']//font[text()='Hudpleje']"
    select_product = "Hudpleje"

    product = "//a[@href='/categories/ansigtscreme']"
    sub_product = "//a[@href='/decubal-face-creme-75-ml-224997']"



    add_cart = "//a[@class='btn btn-primary btn-lg']"
    goto_basket = "//a[contains(text(),' Gå til kurv')]"
    empty_basket = "//a[contains(text(),'Fjern')]"


    ckie_button = "//button[@class='coi-banner__accept']"


    def __init__(self, driver):
        self.driver = driver


    def cookie_button(self):
        self.driver.find_element(By.XPATH, self.ckie_button).click()
    def add_items(self):
        menu_element = self.driver.find_element(By.LINK_TEXT, self.select_product)
        ActionChains(self.driver).move_to_element(menu_element).perform()
        time.sleep(3)

        submenu_element = self.driver.find_element(By.XPATH, self.product)
        submenu_element.click()
        time.sleep(3)
    def click_subProduct(self):
        self.driver.find_element(By.XPATH, self.sub_product).click()

    def add_toCart(self):
        self.driver.find_element(By.XPATH, self.add_cart).click()
    def checkOut(self):
        self.driver.find_element(By.XPATH, self.goto_basket).click()

    def emptyBasket_button(self):
        self.driver.find_element(By.XPATH, self.empty_basket).click()



