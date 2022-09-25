import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.flipkart.com/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']").click()

driver.find_element(By.XPATH,"//img[@alt='Mobiles']").click()


actions = ActionChains(driver)
element1= driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/div/div/span[1]")
# element2 = driver.find_element(By.XPATH,"//a[@title='Realme']")
actions.move_to_element(element1).click().perform()
actions.move_to_element(driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/div/div/div/div[1]/a[3]")).click().perform()

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]")))
# element.click()
actions.context_click(element).perform()


# screen shots

driver.get_screenshot_as_file("sample.png")
# Wait concepts
# Implicit wait
# Explicit wait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# wait = WebDriverWait(driver,10)
# element = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"elemenent")))
# element.click()

time.sleep(5)
driver.close()

