from selenium import webdriver
import time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def selenium_getdata(username,password,startDate,endDate):
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

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()
    time.sleep(2)

    # Find the dropdown element by ID
    dropdown = Select(driver.find_element(By.ID, 'period'))
    dropdown.select_by_value('custom')

    startTime = datetime(*startDate)  # [2022, 6, 5]
    endTime = datetime(*endDate)  # [2023, 6, 19]
    timeDelta = endTime - startTime
    iterations = timeDelta.days
    queryWindow = 7  # Days between start and end dates for the queries

    start_date_texts = []
    duration_texts = []
    station_name_start_texts = []
    station_name_end_texts = []
    ride_price_texts = []
    for i in range(round(iterations/queryWindow)+1):
        startTime_field = driver.find_element(By.ID, 'date[start]')
        endTime_field = driver.find_element(By.ID, 'date[end]')
        startTime_field.send_keys(startTime.strftime('%d-%m-%Y'))
        startTime = startTime + timedelta(days=queryWindow)
        endTime_field.send_keys(startTime.strftime('%d-%m-%Y'))
        actions = ActionChains(driver)

        # Click somewhere
        actions.move_by_offset(0, 0).click().perform()
        time.sleep(1)
        # Copy page contents
        page_contents = BeautifulSoup(driver.page_source, 'html.parser')
        # print(page_contents)

        # Get elements
        start_dates = page_contents.find_all('div', class_='start-date')
        start_date_texts = start_date_texts + [j.text.strip() for j in start_dates]
        duration = page_contents.find_all('div', class_='duration')
        duration_texts = duration_texts + [j.text.strip() for j in duration]
        station_name_start = page_contents.find_all('div', class_='start-station-name-block')
        station_name_start_texts = station_name_start_texts + [j.text.strip() for j in station_name_start if j.text.strip() != '' and not j.text.strip().startswith("Bike ID")]
        station_name_end = page_contents.find_all('div', class_='end-station-name-block')
        station_name_end_texts = station_name_end_texts + [j.text.strip() for j in station_name_end if j.text.strip() != '' and not j.text.strip().startswith("Price")]
        ride_price_texts = ride_price_texts + [j.text.strip() for j in station_name_end if j.text.strip().startswith("Price")]


    driver.quit()

    print(start_date_texts)
    print(duration_texts)
    print(station_name_start_texts)
    print(station_name_end_texts)
    print(ride_price_texts)
    print(len(start_date_texts))
    print(len(duration_texts))
    print(len(station_name_start_texts))
    print(len(station_name_end_texts))
    print(len(ride_price_texts))

    with open('list_file.txt', 'w') as file:
        file.write(', '.join(start_date_texts))
        file.write('\n')
        file.write(', '.join(duration_texts))
        file.write('\n')
        file.write(', '.join(station_name_start_texts))
        file.write('\n')
        file.write(', '.join(station_name_end_texts))
        file.write('\n')
        file.write(', '.join(ride_price_texts))

# Test
# selenium_getdata('@gmail.com','',[2022, 6, 5],[2023, 6, 5])