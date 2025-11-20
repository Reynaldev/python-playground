from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome service and driver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# Firefox service and driver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

import time

elemen_list = []

# Set up Chrome options (Optional)
# Only supports Chromium version == 114

# options = webdriver.ChromeOptions() 
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# Set up Firefox options
options = webdriver.FirefoxOptions()

# Use a proper service object
service = Service(GeckoDriverManager().install())

for page in range(1, 3):
    # Initialize driver properly
    driver = webdriver.Firefox(service=service, options=options)

    # Load the URL
    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page}"
    driver.get(url)
    time.sleep(2)   # Optional wait to ensure page loads

    # Extract product details
    titles = driver.find_elements(By.CLASS_NAME, "title")
    prices = driver.find_elements(By.CLASS_NAME, "price")
    descriptions = driver.find_elements(By.CLASS_NAME, "description")
    ratings = driver.find_elements(By.CLASS_NAME, "ratings")

    # Store results in a list
    for i in range(len(titles)):
        elemen_list.append([
            titles[i].text,
            prices[i].text,
            descriptions[i].text,
            ratings[i].text
        ])

    driver.quit()

# Display the extracted data
for row in elemen_list:
    print(row)
