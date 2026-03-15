import allure
from selenium.webdriver.common.by import By
from data import Urls
from locators.faq_locators import FaqLocators
from pages.base_page import BasePage

class QuestionsPage(BasePage):

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    FAQ_ACCORDION = (By.CLASS_NAME, "accordion")

    @allure.step("Открытие главной страницы и принятие куки")
    def open_main_page(self):
        self.browser.get(Urls.MAIN_PAGE_URL)
        try:
            self.click_element(self.COOKIE_BUTTON, time=3)
        except:
            pass 
        return self

    @allure.step("Скролл к разделу 'Вопросы о важном'")
    def scroll_to_faq(self):
        self.scroll_to_element(self.FAQ_ACCORDION)
        return self

    @allure.step("Клик по вопросу и получение текста ответа")
    def get_answer_text(self, index):
        real_id = index - 1
        
        method_q, locator_q = FaqLocators.QUESTION
        method_a, locator_a = FaqLocators.ANSWER

        q_loc = (method_q, locator_q.format(real_id))
        a_loc = (method_a, locator_a.format(real_id))

        self.scroll_to_element(q_loc)
        # Используем  js_click, чтобы картинка самоката не мешала
        self.js_click(q_loc) 
        
        return self.get_text(a_loc)









