import allure
import pytest
from data import QuestionsAndAnswers
from pages.faq_page import QuestionsPage 

class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на вопрос открывается соответствующий текст ответа')
    
    @pytest.mark.parametrize('index, question, expected_answer', QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST)
    def test_check_question_and_answer(self, browser, index, question, expected_answer):
        # 1. Инициализация страницы
        faq_page = QuestionsPage(browser)
        
        # 2. Открытие главной страницы и принятие куки
        faq_page.open_main_page()
        
        # 3. Скролл к разделу с вопросами
        faq_page.scroll_to_faq()
        
        # 4. Получение текста ответа (кликая по индексу)
        actual_answer = faq_page.get_answer_text(index)
        
        # 5. Явный ASSERT
        assert actual_answer == expected_answer, (
            f"Ошибка в вопросе №{index} ('{question}'). "
            f"Ожидали: {expected_answer}, получили: {actual_answer}"
        )

        

