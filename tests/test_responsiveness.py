from selenium import webdriver
import pytest

def test_mobile_responsiveness():
    options = webdriver.ChromeOptions()
    mobile_emulation = { "deviceName": "iPhone X" }
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.apple.com")
    assert "Apple" in driver.title
    driver.save_screenshot("screenshots/responsiveness.png")
    driver.quit()
