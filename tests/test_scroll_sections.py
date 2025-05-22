from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_scroll_content_loading():
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.apple.com")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    footer = driver.find_element("css selector", "footer")
    assert footer.is_displayed()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    driver.save_screenshot(f"screenshots/bag_icon_{timestamp}.png")
    driver.quit()
