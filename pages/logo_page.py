import allure
from data import Urls
from locators.order_locators import OrderLocators
from locators.logo_locators import LogoLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LogoPage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.browser.get(Urls.MAIN_PAGE_URL)
        return self

    @allure.step("Клик по кнопке 'Заказать' в шапке")
    def click_order_button(self):
        self.browser.find_element(*OrderLocators.ORDER_BUTTON_HEADER).click()
        return self

    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_button(self):
        self.browser.find_element(*LogoLocators.SCOOTER_BUTTON).click()
        return self

    @allure.step("Клик по логотипу 'Яндекс' (Дзен)")
    def click_dzen_button(self):
        self.browser.find_element(*LogoLocators.YANDEX_BUTTON).click()
        return self

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_tab(self):
        # Ожидаем, что откроется вторая вкладка
        WebDriverWait(self.browser, 10).until(lambda d: len(d.window_handles) > 1)
        self.browser.switch_to.window(self.browser.window_handles[1])
        return self

    @allure.step("Ожидание загрузки страницы Дзена")
    def wait_for_dzen_load(self):
        # Используем url_contains, так как к URL Дзена могут добавляться параметры
        WebDriverWait(self.browser, 10).until(ec.url_contains("dzen.ru"))
        return self

    @allure.step("Проверка URL страницы Дзена")
    def should_be_dzen_url(self):
        assert "dzen.ru" in self.browser.current_url
        return self

    @allure.step("Проверка возврата на главную страницу 'Самоката'")
    def should_be_main_page_url(self):
        assert self.browser.current_url == Urls.MAIN_PAGE_URL
        return self
