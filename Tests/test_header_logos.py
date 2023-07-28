import allure
from Pages.main_page import MainPage

class TestHeaderButtons():
    @allure.title('Проверка клика на лого Самокат')
    def test_click_logo_scooter(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        main_page.click_logo_scooter()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Проверка клика на лого Яндекс')
    def test_click_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        main_page.switch_window()
        assert driver.current_url == "https://dzen.ru/?yredirect=true"