from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

def test_hero_image_visibility():
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.apple.com")
    hero_image = driver.find_element("css selector", "section.hero img, section.hero picture")
    assert hero_image.is_displayed()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    driver.save_screenshot(f"screenshots/bag_icon_{timestamp}.png")
    driver.quit()
