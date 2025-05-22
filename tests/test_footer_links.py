from selenium import webdriver
import pytest

def test_footer_links_presence():
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.apple.com")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    footer_links = driver.find_elements("css selector", "footer a")
    assert len(footer_links) > 0
    driver.save_screenshot("screenshots/footer_links.png")
    driver.quit()
