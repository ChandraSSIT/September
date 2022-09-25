import time

from selenium import  webdriver
from selenium.webdriver.common.by import By



def Login_Page():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    time.sleep(5)
    driver.find_element(By.ID,"login-button").click()
    element = driver.find_element(By.XPATH,"//span[@class='title']")
    return True

def Invalid_Login_Page():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID,"user-name").send_keys("standard_user1")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    time.sleep(5)
    driver.find_element(By.ID,"login-button").click()
    element = driver.find_element(By.XPATH,"//h3[@data-test='error']")
    return element.text

Invalid_Login_Page()