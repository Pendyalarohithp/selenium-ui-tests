from selenium import webdriver
import pytest

def test_bag_icon_opens_cart():
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.apple.com")
    bag_icon = driver.find_element("css selector", "a.ac-gn-link-bag")
    bag_icon.click()
    mini_cart = driver.find_element("id", "ac-gn-bagview-content")
    assert mini_cart.is_displayed()
    driver.save_screenshot("screenshots/bag_icon.png")
    driver.quit()
