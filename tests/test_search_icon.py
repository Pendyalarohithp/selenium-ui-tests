from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

def test_search_icon():
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.apple.com")
    search_icon = driver.find_element("css selector", "a.ac-gn-link-search")
    search_icon.click()
    search_input = driver.find_element("id", "ac-gn-searchform-input")
    assert search_input.is_displayed()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    driver.save_screenshot(f"screenshots/bag_icon_{timestamp}.png")
    driver.quit()
