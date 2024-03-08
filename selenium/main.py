from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element(By.ID, "#bigCookie")
start_time = time.time()
timeout = start_time + 60*5

while(True):
    if time.time() > timeout:
        break
    if time.time() % 5 == 0:

    cookie.click()

# driver.quit()
