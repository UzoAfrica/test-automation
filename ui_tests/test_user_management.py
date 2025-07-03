from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login")
    driver.maximize_window()
    yield driver
    driver.quit()

def login(driver):
    driver.find_element(By.ID, "email").send_keys("admin@techcorp.com")
    driver.find_element(By.ID, "password").send_keys("AdminPass123!")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)

def test_user_crud_workflow(driver):
    login(driver)

    # Create a user
    driver.find_element(By.ID, "addUserBtn").click()
    driver.find_element(By.ID, "firstName").send_keys("Test")
    driver.find_element(By.ID, "lastName").send_keys("User")
    driver.find_element(By.ID, "email").send_keys("test.user@techcorp.com")
    driver.find_element(By.ID, "submitUser").click()
    time.sleep(1)
    assert "test.user@techcorp.com" in driver.page_source

    # Edit user
    driver.find_element(By.XPATH, "//td[contains(text(), 'test.user')]/..//button[text()='Edit']").click()
    driver.find_element(By.ID, "title").clear()
    driver.find_element(By.ID, "title").send_keys("QA Engineer")
    driver.find_element(By.ID, "submitUser").click()
    time.sleep(1)
    assert "QA Engineer" in driver.page_source

    # Delete user
    driver.find_element(By.XPATH, "//td[contains(text(), 'test.user')]/..//button[text()='Delete']").click()
    driver.switch_to.alert.accept()
    time.sleep(1)
    assert "test.user@techcorp.com" not in driver.page_source
