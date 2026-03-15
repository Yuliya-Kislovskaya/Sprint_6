import allure
from locators.order_locators import OrderLocators
from data import Urls
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.browser.get(Urls.MAIN_PAGE_URL)
        return self

    @allure.step("Клик по кнопке 'Заказать' в шапке")
    def click_header_order_button(self):
        self.click_element(OrderLocators.ORDER_BUTTON_HEADER)
        return self

    @allure.step("Клик по кнопке 'Заказать' в центре страницы")
    def click_center_order_button(self):
        self.scroll_to_element(OrderLocators.ORDER_CENTER_BUTTON)
        self.click_element(OrderLocators.ORDER_CENTER_BUTTON)
        return self

    @allure.step("Заполнение первой части формы (Персональные данные)")
    def fill_user_data(self, name, last_name, address, metro_name, phone):
        self.send_keys(OrderLocators.NAME, name)
        self.send_keys(OrderLocators.LAST_NAME, last_name)
        self.send_keys(OrderLocators.ADDRESS, address)
        self.send_keys(OrderLocators.METRO, metro_name)
        # Добавляем поиск элемента, чтобы дождаться появления выпадающего списка
        self.find_element(OrderLocators.LIST_STATION) 
        self.click_element(OrderLocators.LIST_STATION)
        self.send_keys(OrderLocators.NUMBER, phone)
        self.click_element(OrderLocators.NEXT_BUTTON)
        return self


    @allure.step("Выбор даты доставки")
    def set_delivery_date(self, date_value):
        self.send_keys(OrderLocators.DATE_DELIVERY, date_value)
        self.send_keys(OrderLocators.DATE_DELIVERY, Keys.ENTER)
        return self

    @allure.step("Выбор срока аренды")
    def set_rental_time(self, day_text):
        self.click_element(OrderLocators.RENT_TIME)
        
        dynamic_locator = (
            OrderLocators.SELECT_RENT_TIME[0], 
            OrderLocators.SELECT_RENT_TIME[1].format(day_text)
        )
        self.click_element(dynamic_locator)
        return self

    @allure.step("Выбор цвета и комментария")
    def set_additional_info(self, color, comment):
        if color == 'чёрный жемчуг':
            self.click_element(OrderLocators.BLACK_COLOR_CHECKBOX)
        elif color == 'серая безысходность':
            self.click_element(OrderLocators.GREY_COLOR_CHECKBOX)
        self.send_keys(OrderLocators.COMMENT, comment)
        return self

    @allure.step("Финальное подтверждение заказа")
    def confirm_order(self):
        self.click_element(OrderLocators.ORDER_BUTTON)
        self.click_element(OrderLocators.YES_BUTTON)
        return self

    @allure.step("Проверка текста успешного заказа")
    def get_success_message(self):
        return self.get_text(OrderLocators.ORDER_COMPLETED)

