from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_chrome_driver(headless=False, mobile=False):
    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")

    chrome_options.add_argument("--window-size=1920,1080")

    if mobile:
        device_emulation = {
            "deviceName": "iPhone X"
        }
        chrome_options.add_experimental_option("mobileEmulation", device_emulation)

    driver = webdriver.Chrome(options=chrome_options)
    return driver
