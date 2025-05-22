import os
import re

tests_dir = "tests"
wait_imports = (
    "from selenium.webdriver.common.by import By\n"
    "from selenium.webdriver.support.ui import WebDriverWait\n"
    "from selenium.webdriver.support import expected_conditions as EC\n"
)

def update_element_calls(content):
    # Convert find_element
    content = re.sub(
        r'driver\.find_element\("([^"]+)",\s*"([^"]+)"\)',
        lambda m: f'WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.{m.group(1).replace(" ", "_").upper()}, "{m.group(2)}")))',
        content
    )

    # Convert find_elements
    content = re.sub(
        r'driver\.find_elements\("([^"]+)",\s*"([^"]+)"\)',
        lambda m: (
            f'WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.{m.group(1).replace(" ", "_").upper()}, "{m.group(2)}")))\n'
            f'    footer_links = driver.find_elements(By.{m.group(1).replace(" ", "_").upper()}, "{m.group(2)}")'
        ),
        content
    )

    return content

def update_files():
    for filename in os.listdir(tests_dir):
        if filename.endswith(".py"):
            path = os.path.join(tests_dir, filename)
            with open(path, "r") as file:
                content = file.read()

            if "WebDriverWait" not in content:
                content = wait_imports + content
            content = update_element_calls(content)

            with open(path, "w") as file:
                file.write(content)
            print(f"✅ Updated: {filename}")

update_files()
