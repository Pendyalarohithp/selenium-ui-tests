from selenium import webdriver
import pytest

def test_aria_labels():
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.apple.com")
    elements_with_aria = driver.find_elements("css selector", "[aria-label]")
    assert len(elements_with_aria) > 0
    driver.save_screenshot("screenshots/screen_reader.png")
    driver.quit()
