from selenium import webdriver
import pytest

def test_homepage_load():
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.apple.com")
    assert "Apple" in driver.title
    driver.save_screenshot("screenshots/homepage_load.png")
    driver.quit()
