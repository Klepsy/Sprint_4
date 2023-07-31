import allure
from Pages.main_page import MainPage
from Pages.order_page import OrderPage

class TestOrderPage():
    @allure.title('Проверка оформления заказа "Чёрный жемчуг"')
    def test_order_black(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_button_order_up()
        order_page.fill_order_data1()
        order_page.continue_make_order()
        order_page.fill_order_data2()
        order_page.choose_black_scooter()
        order_page.click_make_order()
        assert order_page.confirm_order() == "Отменить заказ"

    @allure.title('Проверка оформления заказа "Серая безысходность"')
    def test_order_grey(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_button_order_up()
        order_page.fill_order_data1()
        order_page.continue_make_order()
        order_page.fill_order_data2()
        order_page.choose_grey_scooter()
        order_page.click_make_order()
        assert order_page.confirm_order() == "Отменить заказ"