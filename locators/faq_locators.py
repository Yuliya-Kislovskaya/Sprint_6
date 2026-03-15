from selenium.webdriver.common.by import By

class FaqLocators:
    QUESTION = (By.ID, "accordion__heading-{}")
    ANSWER = (By.ID, "accordion__panel-{}")




