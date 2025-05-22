from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

def test_logo_redirect():
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.apple.com")
    logo = driver.find_element("css selector", "a.ac-gn-link-apple")
    logo.click()
    assert "apple.com" in driver.current_url
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    driver.save_screenshot(f"screenshots/bag_icon_{timestamp}.png")
    driver.quit()
