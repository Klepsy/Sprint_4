import allure
from Locators.Locators import OrderPageLocators as OPL
from Pages.base_page import BasePage
from selenium.webdriver import Keys
from helper import User

class OrderPage(BasePage):
    @allure.step('Вводим имя')
    def enter_name(self):
        self.set_text_into_field(OPL.field_name, User.name)

    @allure.step('Вводим фамилию')
    def enter_last_name(self):
        self.set_text_into_field(OPL.field_last_name, User.last_name)

    @allure.step('Вводим адрес')
    def enter_address_name(self):
        self.set_text_into_field(OPL.field_address, User.address)

    @allure.step('Выбираем станцию метро')
    def enter_metro_station(self):
        self.click_on_element(OPL.field_subway_station)
        self.driver.find_element(*OPL.field_subway_station).send_keys(Keys.ARROW_DOWN+Keys.ENTER)

    @allure.step('Вводим номер телефона')
    def enter_phone_number(self):
        self.set_text_into_field(OPL.field_phone_number, User.phone)

    @allure.step('Продолжаем оформлять заказ, кликнув по внопке "Далее"')
    def continue_make_order(self):
        self.click_on_element(OPL.button_next)

    @allure.step('Вводим дату доставки')
    def enter_delivery_date(self):
        self.set_text_into_field(OPL.field_when_to_bring, User.delivery_date)

    @allure.step('Вводим срок аренды')
    def enter_rental_period(self):
        self.click_on_element(OPL.field_rental_period)
        self.wait_for_loading(OPL.four_days_rental_period)
        self.click_on_element(OPL.four_days_rental_period)

    @allure.step('Цвет скутера - черный жемчуг')
    def choose_black_scooter(self):
        self.click_on_element(OPL.scooter_color_black)

    @allure.step('Цвет скутера - серая безысходность')
    def choose_grey_scooter(self):
        self.click_on_element(OPL.scooter_color_grey)

    @allure.step('Оставляем комментарий')
    def enter_comment_courier(self):
        self.set_text_into_field(OPL.field_comment, User.comment)

    @allure.step('Оформляем заказ по кнопке "Заказать"')
    def click_make_order(self):
        self.click_on_element(OPL.button_to_order)

    @allure.step('Подтверждаем заказ')
    def confirm_order(self):
        self.wait_for_loading(OPL.yes_button)
        self.click_on_element(OPL.yes_button)
        self.wait_for_loading(OPL.button_check_status)
        self.click_on_element(OPL.button_check_status)
        self.wait_for_loading(OPL.cancel_order_button)
        return self.get_text_of_the_element(OPL.cancel_order_button)

