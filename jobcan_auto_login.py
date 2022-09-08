from dotenv import load_dotenv
from selenium import webdriver
from time import sleep
import os
import chromedriver_binary

load_dotenv()
jobcan_login_id = os.getenv("JOBCAN_LOGIN_ID")
jobcan_login_password = os.getenv("JOBCAN_LOGIN_PASSWORD")


def jobcan_automation(arg):
    try:
        driver = webdriver.Chrome()
        driver.get("https://id.jobcan.jp/users/sign_in")
        sleep(1)

        login_id = driver.execute_script("return document.querySelector('#user_email')").send_keys(jobcan_login_id)
        sleep(1)

        password = driver.execute_script("return document.querySelector('#user_password')").send_keys(
            jobcan_login_password)
        sleep(1)

        submit = driver.execute_script("return document.querySelector('#login_button')").click()
        sleep(1)

        driver.execute_script("return document.querySelector('#jbc-app-links > ul > li:nth-child(3) > a')").click()
        sleep(1)
        if arg == 0:
            driver.execute_script("return document.querySelector('#adit-button-work-start')").click()
            return
        if arg == 1:
            driver.execute_script("return document.querySelector('#adit-button-work-end')").click()
        driver.close()
        return 1

    except:
        return 0
