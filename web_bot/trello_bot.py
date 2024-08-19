from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import date
import os
import json

# https://googlechromelabs.github.io/chrome-for-testing/
# CHROME_DRIVER_PATH = os.path.join(os.getcwd(), 'chromedriver.exe')
OP = webdriver.ChromeOptions()
OP.add_argument('--headless')
DRIVER = webdriver.Chrome()   

def screenshotPage():
    time.sleep(2)
    date_str = date.today().strftime("%d-%m-%Y")
    fpath = os.path.join(os.getcwd(), 'downloads/{}.png'.format(date_str))
    DRIVER.get_screenshot_as_file(fpath)

def login():
    with open('config.json') as configFile:
        credentials = json.load(configFile)
        time.sleep(2)
        DRIVER.find_element(By.XPATH, value="//a[@href='https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3Fdisplay%3DeyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%253D%253D&display=eyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%3D%3D']").click()
        time.sleep(2)
        username = DRIVER.find_element(By.CSS_SELECTOR, value="input[name='username']")
        username.clear()
        username.send_keys(credentials["USERNAME"])
        DRIVER.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        password = DRIVER.find_element(By.CSS_SELECTOR, value="input[name='password']")
        password.clear()
        password.send_keys(credentials["PASSWORD"])
        DRIVER.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

def navigateToBoard():
    time.sleep(5)
    DRIVER.find_element(By.XPATH, value="//div[@title='{}']/ancestor::a".format('Bot Board')).click()
    time.sleep(5)

def addTask():
    time.sleep(2)
    DRIVER.find_element(By.XPATH, value="//textarea[@aria-label='To Do']/ancestor::div/descendant::button[@data-testid='list-add-card-button']").click()
    task_text_area = DRIVER.find_element(By.XPATH, value="//textarea[@data-testid='list-card-composer-textarea']")
    task_text_area.clear()
    task_text_area.send_keys("Bot Added Task")
    DRIVER.find_element(By.XPATH, value="//button[@data-testid='list-card-composer-add-card-button']").click()
    time.sleep(5)

def main():
    try:
        DRIVER.get("https://trello.com")
        DRIVER.maximize_window()
        login()
        navigateToBoard()
        addTask()
        screenshotPage()
        input("Bot Operation Completed. Press any key...")
    except Exception as e:
        print(e)
        DRIVER.close()
    
if __name__ == "__main__":
    main()