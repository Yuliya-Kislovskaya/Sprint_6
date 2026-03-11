import allure
import pytest
from data import OrderData

class TestOrderPage:
    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных и разными точками входа')
    @pytest.mark.parametrize('button_method, data_order', [
        ('click_first_button', OrderData.FIRST_ORDER),
        ('click_second_button', OrderData.SECOND_ORDER)
    ])
    def test_make_an_order(self, order_page, data_order, button_method):
        # 1. Открытие главной страницы
        order_page.open_main_page()
        
        # 2. Клик по кнопке "Заказать" (через getattr выбираем нужный метод из фикстуры)
        getattr(order_page, button_method)()
        
        # 3. Выполнение полного цикла заказа (используем распаковку словаря **)
        order_page.full_order_flow(**data_order)
        
        # 4. Финальная проверка уже встроена в full_order_flow, 
        # но можно вызвать отдельно для наглядности в отчете:
        order_page.check_confirmation_window()
