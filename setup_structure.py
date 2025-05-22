import os

# Define folders and test case filenames
folders = ['run_tests', 'tests', 'screenshots']
test_cases = [
    "test_homepage.py",
    "test_logo_redirect.py",
    "test_top_nav_links.py",
    "test_search_icon.py",
    "test_bag_icon.py",
    "test_scroll_sections.py",
    "test_responsiveness.py",
    "test_footer_links.py",
    "test_hero_image.py",
    "test_screen_reader.py"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty test files
for filename in test_cases:
    filepath = os.path.join('tests', filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write("# UI test placeholder for: " + filename + "\n")

# Create run_tests.py with a basic test runner
run_tests_path = os.path.join('run_tests', 'run_tests.py')
if not os.path.exists(run_tests_path):
    with open(run_tests_path, 'w') as f:
        f.write('''import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    testRunner = unittest.runner.TextTestRunner()
    testRunner.run(tests)
''')

print("✅ Project structure created.")
