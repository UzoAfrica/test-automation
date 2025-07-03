import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def wait_for_notification(driver, keyword, timeout=10):
    for _ in range(timeout):
        if keyword in driver.page_source:
            return True
        time.sleep(1)
    return False

def test_real_time_notification_appears():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/dashboard")
    driver.maximize_window()

    # Simulate: Open notification area
    driver.find_element(By.ID, "notificationIcon").click()

    # Wait for update — this assumes another process triggers it
    assert wait_for_notification(driver, "New user created")

    driver.quit()
