import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

def test_mobile_responsiveness():
    options = webdriver.ChromeOptions()
    mobile_emulation = { "deviceName": "iPhone X" }
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.apple.com")
    assert "Apple" in driver.title
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    driver.save_screenshot(f"screenshots/bag_icon_{timestamp}.png")
    driver.quit()
