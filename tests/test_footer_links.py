import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

def test_footer_links_presence():
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.apple.com")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    footer_links = driver.find_elements("css selector", "footer a")
    assert len(footer_links) > 0
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    driver.save_screenshot(f"screenshots/bag_icon_{timestamp}.png")
    driver.quit()
