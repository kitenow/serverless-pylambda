import json
import time
import datetime
import selenium
from selenium import webdriver

def init_selenium():
    driverPath = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(driverPath, options=options)
    driver.implicitly_wait(7)
    print("Chrome Load Complete")
    return driver

def fn_start(event, context):

    print('fn_start lisening...ok!')

    driver = init_selenium()

    print(driver)


    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
