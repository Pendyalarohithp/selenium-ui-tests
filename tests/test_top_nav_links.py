from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

def test_top_nav_links():
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.apple.com")
    nav_links = driver.find_elements("css selector", "ul.ac-gn-list > li > a")
    assert len(nav_links) > 0
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    driver.save_screenshot(f"screenshots/bag_icon_{timestamp}.png")
    driver.quit()
