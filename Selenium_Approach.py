from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set the path to your ChromeDriver executable
webdriver_service = Service('./chromeDriver/chromedriver.exe')

# Set up the Chrome options
chrome_options = Options()
#chrome_options.add_argument('--headless')  # Run Chrome in headless mode

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open the page
driver.get('https://members.bikesharetoronto.com/trips')

# Sign in
username_field = driver.find_element(By.ID, 'userName')
password_field = driver.find_element(By.ID, 'password')
submit_button = driver.find_element(By.CSS_SELECTOR, 'input.button.sign-in.w-button[type="submit"]')

username_field.send_keys('')
password_field.send_keys('')
submit_button.click()
time.sleep(2)

# Find the dropdown element by ID
dropdown = Select(driver.find_element(By.ID, 'period'))
dropdown.select_by_value('custom')
startTime_field = driver.find_element(By.ID, 'date[start]')
endTime_field = driver.find_element(By.ID, 'date[end]')

startTime = "01-05-2023"
endTime = "30-05-2023"
startTime_field.send_keys(startTime)
endTime_field.send_keys(endTime)
actions = ActionChains(driver)

# Click somewhere
actions.move_by_offset(0, 0).click().perform()
time.sleep(1)

# Copy page contents
page_contents = driver.page_source
print(page_contents)

driver.quit()