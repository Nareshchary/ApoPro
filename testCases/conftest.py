from selenium import webdriver
import pytest
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver
