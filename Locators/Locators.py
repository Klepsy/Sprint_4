from selenium.webdriver.common.by import By

class MainPageLocators:
    questions_title = [By.XPATH, ".//div[text()='Вопросы о важном']"]  # Заголовок Вопросы о важном
    questions_list = [By.XPATH, ".//div[@class='accordion']"]  # Гармошка с вопросами и ответами
    questions = [By.XPATH, ".//div[contains(@id, 'accordion__heading-')]"]  # Список вопросов
    answers = [By.XPATH, ".//div[contains(@id, 'accordion__panel-')]/p"]  # Список ответов
    button_order_header = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]  # Кнопка заказа на основной странице
    button_order_middle = [By.XPATH, ".//button[contains(@class, 'Button_Middle__1CSJM')]"]  # Кнопка заказа снизу
    logo_scooter = [By.XPATH, ".//*[@alt='Scooter']"]  # Логотип Самокат
    logo_yandex = [By.XPATH, ".//*[@alt='Yandex']"]  # Логотип Яндекс
    yandex_search_input = [By.XPATH,".//iframe[@class='dzen-search-arrow-common__frame' and @aria-label='Поиск Яндекса']"]  # Поисковая строка Яндекса

class OrderPageLocators:
    field_name = [By.XPATH, ".//input[@placeholder='* Имя']"]  # Поле имени
    field_last_name = [By.XPATH, ".//input[@placeholder='* Фамилия']"]  # Поле Фамилии
    field_address = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]  # Поле адреса
    field_phone_number = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]  # Поле номера телефона
    field_subway_station = [By.XPATH, ".//input[@placeholder='* Станция метро']"]  # Поле выбора метро
    button_next = [By.XPATH, ".//button[text()='Далее']"]  # Кнопка Далее
    field_when_to_bring = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]  # Поле выбора даты доставки
    field_rental_period = [By.XPATH, ".//span[@class='Dropdown-arrow']"]  # Поле срока аренды
    four_days_rental_period = [By.XPATH, ".//div[text()='четверо суток']"]  # Выбор срока аренды 4 дня
    scooter_color_black = [By.XPATH, ".//label[@for='black']"]  # Черный цвет
    scooter_color_grey = [By.XPATH, ".//label[@for='grey']"]  # Серый цвет
    field_comment = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]  # Поле комментария для курьера
    button_to_order = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Заказать']"]  # Кнопка Заказать на странице заказа
    yes_button = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Да']"]  # Кнопка Да
    no_button = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Нет']"] # Кнопка Нет
    button_check_status = [By.XPATH, ".//button[text()='Посмотреть статус']"]  # Кнопка Посмотреть статус
    cancel_order_button = [By.XPATH, ".//button[text()='Отменить заказ']"] # Кнопка Отменить заказ