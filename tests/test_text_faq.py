import allure
import pytest
from data import QuestionsAndAnswers

class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на вопрос открывается соответствующий текст ответа')
    @pytest.mark.parametrize('index, question, answer', QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST)
    def test_check_question_and_answer(self, faq_page, index, question, answer):
        # 1. Открытие главной страницы (через фикстуру faq_page)
        faq_page.open_main_page()
        
        # 2. Скролл к разделу с вопросами
        faq_page.scroll_to_faq()
        
        # 3. Клик по вопросу и получение текста ответа
        # (метод get_answer_text уже содержит в себе клик и ожидание)
        actual_answer = faq_page.get_answer_text(index)
        
        # 4. Проверка, что текст ответа соответствует ожидаемому из data.py
        assert actual_answer == answer, f"Ожидаемый ответ: {answer}, но получен: {actual_answer}"
