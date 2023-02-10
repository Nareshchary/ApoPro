from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class LoginPage:
    ckie_button = "//button[@class='coi-banner__accept']"
    log_hlink = "//a[@href='/Account/Login']"
    textbox_username_id = "Email"
    textbox_password_id = "password"
    button_login = "//input[@id='login-submit']"
    link_logout = "//a[@href='/account/logout/?returnUrl=/logout/']"
    link_t = "Log ud og tøm kurven"
    clk_text = "//span[contains(text(),'Profil')]"

    def __init__(self, driver):
        self.driver = driver

    def login_link(self):
        self.driver.find_element(By.XPATH, self.log_hlink).click()

    def cookie_button(self):
        self.driver.find_element(By.XPATH, self.ckie_button).click()

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout).click()

    def moveTo(self):
        menu_element = self.driver.find_element(By.XPATH, self.clk_text)
        ActionChains(self.driver).move_to_element(menu_element).perform()
        time.sleep(3)
        submenu_element = self.driver.find_element(By.LINK_TEXT, self.link_t)
        submenu_element.click()