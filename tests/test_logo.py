import allure

class TestURL:
    @allure.title('Проверка URL Логотипа "Самокат"')
    def test_main_page(self, logo_page):
        # Открытие главной страницы
        logo_page.open_main_page()
        # Переход на страницу заказа через кнопку в шапке
        logo_page.click_order_button()
        # Клик по логотипу "Самокат"
        logo_page.click_scooter_button()
        # Проверка, что вернулись на главную
        logo_page.should_be_main_page_url()

    @allure.title('Проверка URL Логотипа "Яндекс"')
    def test_dzen_url(self, logo_page):
        # Открытие главной страницы
        logo_page.open_main_page()
        # Клик по логотипу "Яндекс"
        logo_page.click_dzen_button()
        # Переключение на открывшуюся вкладку
        logo_page.switch_to_new_tab()
        # Ожидание загрузки Дзена
        logo_page.wait_for_dzen_load()
        # Проверка URL
        logo_page.should_be_dzen_url()
