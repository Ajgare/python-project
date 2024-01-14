from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import  ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://omayo.blogspotm.com/")
driver.maximize_window()
#driver.save_screenshot("c:\\Users\\student\\Pictures\\Camera Roll.png")
st=Select(driver.find_element((By.ID,'drop1')))
st.select_by_index(2)

