import allure
from Pages.main_page import MainPage
from Pages.order_page import OrderPage

class TestOrderPage():
    @allure.title('Проверка оформления заказа "Чёрный жемчуг"')
    def test_order_black(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_button_order_up()
        order_page.enter_name()
        order_page.enter_last_name()
        order_page.enter_address_name()
        order_page.enter_metro_station()
        order_page.enter_phone_number()
        order_page.continue_make_order()
        order_page.enter_delivery_date()
        order_page.enter_rental_period()
        order_page.choose_black_scooter()
        order_page.enter_comment_courier()
        order_page.click_make_order()
        assert order_page.confirm_order() == "Отменить заказ"

    @allure.title('Проверка оформления заказа "Серая безысходность"')
    def test_order_grey(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_button_order_up()
        order_page.enter_name()
        order_page.enter_last_name()
        order_page.enter_address_name()
        order_page.enter_metro_station()
        order_page.enter_phone_number()
        order_page.continue_make_order()
        order_page.enter_delivery_date()
        order_page.enter_rental_period()
        order_page.choose_grey_scooter()
        order_page.enter_comment_courier()
        order_page.click_make_order()
        assert order_page.confirm_order() == "Отменить заказ"