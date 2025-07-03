import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize("device", [
    {"width": 1920, "height": 1080, "label": "Desktop"},
    {"width": 768, "height": 1024, "label": "Tablet"},
    {"width": 375, "height": 667, "label": "Mobile"}
])
def test_responsive_layout(device):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(device["width"], device["height"])
    driver.get("http://localhost:8000/login")
    time.sleep(1)

    assert "Login" in driver.title  # Adjust as needed
    print(f"Layout loaded correctly on {device['label']}")
    driver.quit()
