import allure
from Pages.base_page import BasePage
from Locators.Locators import MainPageLocators as MPL

class MainPage(BasePage):
    @allure.step('Получить ответ на вопрос в "Вопросы о важном"')
    def get_answer_to_question(self, question, answer):
        self.wait_for_loading(locator=question)
        self.driver.find_element(*question).click()
        self.wait_for_loading(locator=answer)
        return self.driver.find_element(*answer).text

    @allure.step('Кликаем по лого "Яндекс"')
    def click_logo_yandex(self):
        self.wait_for_loading(MPL.logo_yandex)
        self.click_on_element(MPL.logo_yandex)
        self.switch_window()
        self.wait_for_loading(MPL.yandex_search_input)

    @allure.step('Кликаем по логотипу "Самокат"')
    def click_logo_scooter(self):
        self.wait_for_loading(MPL.logo_scooter)
        self.click_on_element(MPL.logo_scooter)

    @allure.step('Клик по кнопке "Заказать" в хэдере')
    def click_button_order_up(self):
        self.click_on_element(MPL.button_order_header)

    @allure.step('Клик по кнопке "Заказать" внизу')
    def click_button_order_middle(self):
        self.click_on_element(MPL.button_order_middle)
