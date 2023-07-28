import pytest
import allure
from selenium.webdriver.common.by import By
from Pages.main_page import MainPage
from Locators.Locators import MainPageLocators as MPL

class TestQuestions():
    @pytest.mark.parametrize(
        'question, answer, expected_result',
        [
            [[By.ID, 'accordion__heading-0'], [By.ID, 'accordion__panel-0'], 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
            [[By.ID, 'accordion__heading-1'], [By.ID, 'accordion__panel-1'], 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
            [[By.ID, 'accordion__heading-2'], [By.ID, 'accordion__panel-2'], 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
            [[By.ID, 'accordion__heading-3'], [By.ID, 'accordion__panel-3'], 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
            [[By.ID, 'accordion__heading-4'], [By.ID, 'accordion__panel-4'], 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
            [[By.ID, 'accordion__heading-5'], [By.ID, 'accordion__panel-5'], 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
            [[By.ID, 'accordion__heading-6'], [By.ID, 'accordion__panel-6'], 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
            [[By.ID, 'accordion__heading-7'], [By.ID, 'accordion__panel-7'], 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
        ]
    )

    @allure.title('Проверка получения ответов на вопросы')
    def test_get_answers_to_questions(self, driver, question, answer, expected_result):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.scroll_to_questions()
        main_page.wait_for_loading(MPL.questions_list)
        assert main_page.get_answer_to_question(question, answer) == expected_result

