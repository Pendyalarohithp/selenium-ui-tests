from selenium import webdriver
import pytest
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_scroll_content_loading():
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.apple.com")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    footer = driver.find_element("css selector", "footer")
    assert footer.is_displayed()
    driver.save_screenshot("screenshots/scroll_sections.png")
    driver.quit()
