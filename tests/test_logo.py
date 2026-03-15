import allure
from pages.logo_page import LogoPage

class TestURL:
    @allure.title('Проверка URL Логотипа "Самокат"')
    def test_main_page(self, browser):
        logo_page = LogoPage(browser)
        
        logo_page.open_main_page()
        logo_page.click_order_button()
        logo_page.click_scooter_button()
        
        current_url = logo_page.get_current_url()
       
        assert current_url == "https://qa-scooter.praktikum-services.ru/", \
            f"Ожидали главную страницу, но открылся URL: {current_url}"

    @allure.title('Проверка URL Логотипа "Яндекс"')
    def test_dzen_url(self, browser):
        logo_page = LogoPage(browser)
        
        logo_page.open_main_page()
        logo_page.click_dzen_button()
        logo_page.switch_to_new_tab()
        logo_page.wait_for_dzen_load()
        
        current_url = logo_page.get_current_url()
        
        assert "dzen.ru" in current_url, \
            f"Ожидали переход на Дзен, но открылся URL: {current_url}"



