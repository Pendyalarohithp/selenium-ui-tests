from selenium import webdriver
import pytest

def test_top_nav_links():
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.apple.com")
    nav_links = driver.find_elements("css selector", "ul.ac-gn-list > li > a")
    assert len(nav_links) > 0
    driver.save_screenshot("screenshots/top_nav_links.png")
    driver.quit()
