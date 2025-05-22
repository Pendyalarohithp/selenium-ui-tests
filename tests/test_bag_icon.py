from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

def test_bag_icon_opens_cart():
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.apple.com")
    bag_icon = driver.find_element("css selector", "a.ac-gn-link-bag")
    bag_icon.click()
    mini_cart = driver.find_element("id", "ac-gn-bagview-content")
    assert mini_cart.is_displayed()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    driver.save_screenshot(f"screenshots/bag_icon_{timestamp}.png")
    driver.quit()
