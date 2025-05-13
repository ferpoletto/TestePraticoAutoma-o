from selenium import webdriver
from pages.headers_page import HeaderPage
from dotenv import load_dotenv
import os
from utils.selenium_helpers import SeleniumHelpers
 
def before_scenario(context, scenario):    
    load_dotenv()
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(os.getenv("URL_PAGE") )
    context.helpers = SeleniumHelpers(context.driver)    
    context.header = HeaderPage(context.driver, context.helpers)
 
def after_scenario(context):
    context.driver.quit()