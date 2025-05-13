from selenium import webdriver
from utils.selenium_helpers import SeleniumHelpers
from pages.headers_page import HeaderPage
from dotenv import load_dotenv
import os
 
def before_scenario(context, scenario):
    load_dotenv()
    URL_PAGE = os.getenv("URL_PAGE")   
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(URL_PAGE)
    context.header = SeleniumHelpers(context.driver)
 
def after_scenario(context, scenario):
    context.driver.quit()