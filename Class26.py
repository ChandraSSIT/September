# Selenium
# Page object model framework => we are going to access dom as object , with this object we are going to
# access elements and perform actions on that object
# Webdriver => this will access the browser and control this browser and perform UI actions
# different browsers => Chrome , IE, firefox

# API Automation , UI Automation
import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.saucedemo.com/")

driver.maximize_window()

# Locators
# ID
# Name
# Class name
# Xpath
# Css selector path
# text()
# link_text()

# ID
# driver.find_element(By.ID,"user-name").send_keys("standard_user")
# driver.find_element(By.ID,"password").send_keys("secret_sauce")
# time.sleep(5)
# driver.find_element(By.ID,"login-button").click()

# Name

# driver.find_element(By.NAME,"user-name").send_keys("standard_user")
# driver.find_element(By.NAME,"password").send_keys("secret_sauce")
# time.sleep(5)
# driver.find_element(By.NAME,"login-button").click()

# Class Name
# driver.find_element(By.NAME,"user-name").send_keys("standard_user")
# driver.find_element(By.NAME,"password").send_keys("secret_sauce")
# time.sleep(5)
# driver.find_element(By.CLASS_NAME,"submit-button.btn_action").click()

# XPath
# we have two types of XPath => absolute and Relative
# absolute => it will start from root element and it will go till last element, it uses single slash
# Relative => it will try to find element based on parent or based on sibling , it uses double slash
# driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div/input[1]").send_keys("standard_user")
# driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[2]/input").send_keys("secret_sauce")
# time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='login-button']").click()

# CSS selector
# This will generate with >
driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("secret_sauce")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#login-button").click()
time.sleep(2)
text =driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)").text
print(text)



# time.sleep(8)
# driver.close()
# driver.close() # close will close the current tab or current window
# driver.quit() # Quit will close the all tabs or complete browser window

# Drop down
# to read data from drop down we use Select
from selenium.webdriver.support.ui import Select

options =Select(driver.find_element(By.XPATH,"//select[@class='product_sort_container']"))
# options.select_by_index(1)
# options.select_by_value("lohi")
options.select_by_visible_text("Price (low to high)")

# Navigation commands
# driver.back() # to goto previous page
# driver.forward() # to goto next page
# driver.refresh() # to reload the page
# time.sleep(5)
# driver.refresh()
#
# # conditional commands
# driver.find_element(By.ID,"user-name").is_enabled() #this is used to check whether element is enabled to
# # perform any action
# driver.find_element(By.ID,"user-name").is_selected() # to check whether element is selected or not
# driver.find_element(By.ID,"user-name").is_displayed() # to check whether element is displayed
#
# # alerts
# driver.switch_to.alert.accept() # it will click Yes
# driver.switch_to.alert.dismiss() # it will click No

# Scroll bars,Mouse Actions,screenshots,Wait concepts
# Scroll bar
# scroll by pixel
# scroll till element found
# we will do this with javascript
# driver.execute_script("window.scrollBy(0,500)")
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
element  = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
time.sleep(5)
driver.execute_script("arguments[0].scrollIntoView();",element)
time.sleep(10)
driver.close()

