from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

def test_aria_labels():
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.apple.com")
    elements_with_aria = driver.find_elements("css selector", "[aria-label]")
    assert len(elements_with_aria) > 0
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    driver.save_screenshot(f"screenshots/bag_icon_{timestamp}.png")
    driver.quit()
