from selenium import webdriver
import pytest

def test_search_icon():
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.apple.com")
    search_icon = driver.find_element("css selector", "a.ac-gn-link-search")
    search_icon.click()
    search_input = driver.find_element("id", "ac-gn-searchform-input")
    assert search_input.is_displayed()
    driver.save_screenshot("screenshots/search_icon.png")
    driver.quit()
