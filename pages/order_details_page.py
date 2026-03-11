import allure
from locators.order_locators import OrderLocators
from data import Urls
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class OrderPage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.browser.get(Urls.MAIN_PAGE_URL)
        return self

    @allure.step("Клик по кнопке 'Заказать' в шапке")
    def click_first_button(self):
        self.browser.find_element(*OrderLocators.ORDER_BUTTON_HEADER).click()
        return self

    @allure.step("Клик по кнопке Заказать в центре")
    def click_second_button(self):
        element = self.browser.find_element(*OrderLocators.ORDER_CENTER_BUTTON)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        WebDriverWait(self.browser, 5).until(ec.element_to_be_clickable(OrderLocators.ORDER_CENTER_BUTTON)).click()
        return self


    @allure.step("Заполнение поля 'Имя'")
    def user_name(self, name):
        self.browser.find_element(*OrderLocators.NAME).send_keys(name)
        return self

    @allure.step("Заполнение поля 'Фамилия'")
    def user_last_name(self, last_name):
        self.browser.find_element(*OrderLocators.LAST_NAME).send_keys(last_name)
        return self

    @allure.step("Заполнение поля 'Адрес'")
    def user_address(self, address):
        self.browser.find_element(*OrderLocators.ADDRESS).send_keys(address)
        return self

    @allure.step("Выбор станции метро")
    def metro(self, metro_name):
        self.browser.find_element(*OrderLocators.METRO).send_keys(metro_name)
        WebDriverWait(self.browser, 5).until(
        ec.element_to_be_clickable(OrderLocators.LIST_STATION)
        ).click()
        return self

    @allure.step("Заполнение поля 'Телефон'")
    def user_phone(self, phone):
        self.browser.find_element(*OrderLocators.NUMBER).send_keys(phone)
        return self

    @allure.step("Клик по кнопке 'Далее'")
    def click_button_next(self):
        self.browser.find_element(*OrderLocators.NEXT_BUTTON).click()
        return self

    @allure.step("Выбор даты доставки")
    def date_of_delivery(self, date_value):
        date_field = self.browser.find_element(*OrderLocators.DATE_DELIVERY)
        date_field.send_keys(date_value, Keys.ENTER)
        return self

    @allure.step("Выбор срока аренды")
    def rental_time(self, day_text):
        self.browser.find_element(*OrderLocators.RENT_TIME).click()
       
        select_rent_time_locator = (
            OrderLocators.SELECT_RENT_TIME[0], 
            OrderLocators.SELECT_RENT_TIME[1].format(day_text)
        )
        self.browser.find_element(*select_rent_time_locator).click()
        return self

    @allure.step("Выбор цвета самоката")
    def checkbox_color(self, color):
        if color == 'чёрный жемчуг':
            self.browser.find_element(*OrderLocators.BLACK_COLOR_CHECKBOX).click()
        elif color == 'серая безысходность':
            self.browser.find_element(*OrderLocators.GREY_COLOR_CHECKBOX).click()
        return self

    @allure.step("Заполнение комментария для курьера")
    def comment_for_courier(self, comment):
        self.browser.find_element(*OrderLocators.COMMENT).send_keys(comment)
        return self

    @allure.step("Клик по кнопке 'Заказать' под формой")
    def click_button_order(self):
        self.browser.find_element(*OrderLocators.ORDER_BUTTON).click()
        return self

    @allure.step("Подтверждение заказа в модальном окне")
    def click_button_confirmations(self):
        self.browser.find_element(*OrderLocators.YES_BUTTON).click()
        return self

    @allure.step("Проверка успешного оформления заказа")
    def check_confirmation_window(self):
       
        success_text = WebDriverWait(self.browser, 10).until(
            ec.visibility_of_element_located(OrderLocators.ORDER_COMPLETED)
        ).text
        assert 'Заказ оформлен' in success_text
        return self

    @allure.step("Выполнение полного цикла заказа")
    def full_order_flow(self, name, last_name, address, metro, number,
                        delivery_date, rent_days, colour, comment):
        self.user_name(name)
        self.user_last_name(last_name)
        self.user_address(address)
        self.metro(metro)
        self.user_phone(number)
        self.click_button_next()
        self.date_of_delivery(delivery_date)
        self.rental_time(rent_days)
        self.checkbox_color(colour)
        self.comment_for_courier(comment)
        self.click_button_order()
        self.click_button_confirmations()
        self.check_confirmation_window()
        return self
