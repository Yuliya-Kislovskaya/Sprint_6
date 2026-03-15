import allure
import pytest
from data import OrderData
from pages.order_details_page import OrderPage


class TestOrderPage:
    @allure.title('Проверка позитивного сценария заказа самоката')
    @pytest.mark.parametrize('button_method, data_order', [
        ('click_header_order_button', OrderData.FIRST_ORDER), 
        ('click_center_order_button', OrderData.SECOND_ORDER)
    ])
    def test_make_an_order(self, browser, data_order, button_method):
        order_page = OrderPage(browser)
        order_page.open_main_page()
        
        # Выбор кнопки Заказать
        getattr(order_page, button_method)()
        
        # Заполнение формы
        order_page.fill_user_data(
            name=data_order['name'], 
            last_name=data_order['last_name'], 
            address=data_order['address'], 
            metro_name=data_order['metro'], 
            phone=data_order['number']
        )
        
        order_page.set_delivery_date(data_order['delivery_date'])
        order_page.set_rental_time(data_order['rent_days'])
        order_page.set_additional_info(data_order['colour'], data_order['comment'])
        
        order_page.confirm_order()
        
        success_text = order_page.get_success_message()
        assert 'Заказ оформлен' in success_text, f"Текст ошибки: {success_text}"



