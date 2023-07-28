from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл до блока вопросов')
    def scroll_to_questions(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Ожидание загрузки страницы по элементу')
    def wait_for_loading(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Переключение на другую страницу')
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получаем текст элемента')
    def get_text_of_the_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Запись текста в поле')
    def set_text_into_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)