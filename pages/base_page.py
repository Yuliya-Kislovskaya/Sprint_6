import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Поиск элемента {locator}")
    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(
            ec.presence_of_element_located(locator),
            message=f"Не удалось найти элемент: {locator}"
        )

    @allure.step("Клик по элементу {locator}")
    def click_element(self, locator, time=10):
        # Обычный клик с ожиданием кликабельности
        element = WebDriverWait(self.browser, time).until(
            ec.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Клик по элементу через JS {locator}")
    def js_click(self, locator):
        # Клик через JavaScript — игнорирует перекрытия (например, картинку самоката)
        element = self.find_element(locator)
        self.browser.execute_script("arguments[0].click();", element)

    @allure.step("Ввод текста в {locator}")
    def send_keys(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.send_keys(text)

    @allure.step("Скролл к элементу {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Получение текста {locator}")
    def get_text(self, locator, time=10):
        element = WebDriverWait(self.browser, time).until(
            ec.visibility_of_element_located(locator)
        )
        return element.text

    def wait_for_new_tab(self, current_handles_count=1, time=10):
        WebDriverWait(self.browser, time).until(
            lambda d: len(d.window_handles) > current_handles_count
        )

    def wait_for_url_contains(self, url_part, time=15):
        WebDriverWait(self.browser, time).until(ec.url_contains(url_part))

    def get_current_url(self):
        return self.browser.current_url

