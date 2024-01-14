import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://testautomationpractice.blogspot.com")
b = ActionChains(driver)
driver.execute_script("window.scrollBy(0,500)","")
source = driver.find_element(By.XPATH,'//*[@id="draggable"]/p')
target = driver.find_element(By.XPATH,'//*[@id="droppable"]')

b.drag_and_drop(source,target).perform()
