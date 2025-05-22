from selenium import webdriver
import pytest

def test_hero_image_visibility():
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.apple.com")
    hero_image = driver.find_element("css selector", "section.hero img, section.hero picture")
    assert hero_image.is_displayed()
    driver.save_screenshot("screenshots/hero_image.png")
    driver.quit()
