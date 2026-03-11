import pytest
from selenium import webdriver
from pages.faq_page import QuestionsPage      
from pages.logo_page import LogoPage            
from pages.order_details_page import OrderPage  

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def faq_page(browser):
    return QuestionsPage(browser)

@pytest.fixture
def logo_page(browser):
    return LogoPage(browser) 

@pytest.fixture
def order_page(browser):
    return OrderPage(browser) 
