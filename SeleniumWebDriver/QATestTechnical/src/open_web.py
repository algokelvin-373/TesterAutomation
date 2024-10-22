from selenium import webdriver
import time

print("Start to Open Web")
driver = webdriver.Chrome()

print("Open Web Tokopedia")
driver.get("https://www.tokopedia.com/")

print("Delay until 5 Seconds")
time.sleep(5)

print("Close Web")
driver.quit()

print("Finish")
