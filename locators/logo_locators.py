from selenium.webdriver.common.by import By


class LogoLocators:
    # Логотип шапки "Яндекс Самокат"
    SCOOTER_BUTTON = [By.XPATH, ".//a[@href='/']"]
    YANDEX_BUTTON = [By.XPATH, ".//a[@href='//yandex.ru']"]