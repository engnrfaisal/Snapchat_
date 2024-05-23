import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Get Snapchat credentials from environment variables
username = os.getenv("SNAPCHAT_USERNAME")
password = os.getenv("SNAPCHAT_PASSWORD")

# Initialize WebDriver (Assuming using Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run headless Chrome for GitHub Actions
driver = webdriver.Chrome(options=options)

try:
    # Open Snapchat login page
    driver.get("https://accounts.snapchat.com/accounts/login")

    # Login to Snapchat
    user_field = driver.find_element_by_name("username")
    pass_field = driver.find_element_by_name("password")
    user_field.send_keys(username)
    pass_field.send_keys(password)
    pass_field.send_keys(Keys.RETURN)

    time.sleep(5)  # Wait for login to complete

    # Navigate and automate other actions as needed
    # Example: post a snap, send a message, etc.

finally:
    driver.quit()
