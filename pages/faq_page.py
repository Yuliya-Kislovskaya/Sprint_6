import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data import Urls
from locators.faq_locators import FaqLocators

class QuestionsPage:
    def __init__(self, browser):
        self.browser = browser
        self.cookie_button = (By.ID, "rcc-confirm-button")

    @allure.step("Открытие главной страницы и принятие куки")
    def open_main_page(self):
        self.browser.get(Urls.MAIN_PAGE_URL)
        try:
            # Ждем кнопку куки 5 секунд и кликаем. Если нет — идем дальше.
            WebDriverWait(self.browser, 5).until(
                ec.element_to_be_clickable(self.cookie_button)
            ).click()
        except:
            pass
        return self

    @allure.step("Скролл к разделу 'Вопросы о важном'")
    def scroll_to_faq(self):
        # Находим весь блок FAQ
        element = self.browser.find_element(By.CLASS_NAME, "accordion")
        # Центрируем его на экране
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return self

    @allure.step("Клик по вопросу и получение текста ответа")
    def get_answer_text(self, index):
        real_id = index - 1
        
        method_q, locator_q = FaqLocators.QUESTION
        method_a, locator_a = FaqLocators.ANSWER

        q_loc = (method_q, locator_q.format(real_id))
        a_loc = (method_a, locator_a.format(real_id))

        # Ожидаем вопрос, скроллим к нему и жмем через JS (чтобы не мешали картинки)
        question_el = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(q_loc))
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", question_el)
        self.browser.execute_script("arguments[0].click();", question_el)

        # Ждем появления текста ответа и возвращаем его
        answer_el = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(a_loc))
        return answer_el.text







