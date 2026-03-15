import allure
from locators.order_locators import OrderLocators
from locators.logo_locators import LogoLocators
from pages.base_page import BasePage
from data import Urls

class LogoPage(BasePage):

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.browser.get(Urls.MAIN_PAGE_URL)
        return self

    @allure.step("Клик по кнопке 'Заказать' в шапке")
    def click_order_button(self):
        self.click_element(OrderLocators.ORDER_BUTTON_HEADER)
        return self

    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_button(self):
        self.click_element(LogoLocators.SCOOTER_BUTTON)
        return self

    @allure.step("Клик по логотипу 'Яндекс' (Дзен)")
    def click_dzen_button(self):
        self.click_element(LogoLocators.YANDEX_BUTTON)
        return self

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_tab(self):
        # Ожидаем появления второй вкладки
        self.wait_for_new_tab(current_handles_count=1)
        # Переключаемся на последнюю открытую
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return self

    @allure.step("Ожидание загрузки страницы Дзена")
    def wait_for_dzen_load(self):
        self.wait_for_url_contains("dzen.ru")
        return self


