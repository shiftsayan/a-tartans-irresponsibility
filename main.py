from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from secrets import username, password

if __name__ == "__main__":
    # Start Selenium
    driver = webdriver.Chrome('./chromedriver')
    
    # Log into Student Daily Self-Assessment
    driver.get('https://daily-student.cmu.edu/')
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="passwordinput"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="formwrapper"]/div[4]/input').click()

    # Wait for Student Daily Self-Assessment to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="Field12_1"]'))
    )

    # Fill in Student Daily Self-Assessment
    driver.find_element_by_xpath('//*[@id="Field12_1"]').click() # No close contact with someone diagnosed with COVID-19
    driver.find_element_by_xpath('//*[@id="Field3_1"]').click() # No symptoms of COVID-19 in the last 24 hours
    driver.find_element_by_xpath('//*[@id="Field5_2"]').click() # No temperature check today
    
    # Submit Student Daily Self-Assessment
    driver.find_element_by_xpath('//*[@id="saveForm"]').click()

    # Close Selenium
    driver.quit()
