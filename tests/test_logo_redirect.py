from selenium import webdriver
import pytest

def test_logo_redirect():
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.apple.com")
    logo = driver.find_element("css selector", "a.ac-gn-link-apple")
    logo.click()
    assert "apple.com" in driver.current_url
    driver.save_screenshot("screenshots/logo_redirect.png")
    driver.quit()
