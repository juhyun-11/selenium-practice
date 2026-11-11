#pages.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value)))

def wait_invisible(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located((by, value)))
