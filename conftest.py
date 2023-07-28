import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    driver.maximize_window()
    yield driver
    driver.quit()
