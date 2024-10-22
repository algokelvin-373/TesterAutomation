from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass

print("-----Start to Open Web-----")
driver = webdriver.Chrome()

print("1. Open Web Tokopedia Login")
driver.get("https://www.tokopedia.com/login")

print("2. Input Data Email")
# input_email = driver.find_element(By.XPATH, "//div[@class='css-vyote']/input")
# if input_email.is_displayed():
#     print("Element is visible.")
#     input_email.send_keys("email123@gmail.com")
# else:
#     print("Element is not visible yet.")
# input_email.send_keys("kelvin373.ht@gmail.com")
# btn_next = driver.find_element(By.XPATH, "//*[@id='email-phone-submit']")
# btn_next.click()
input_email = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@name='login']"))
)
input_email.send_keys("email123@gmail.com")

# time.sleep(5)
#
# print("3. Input Password")
# input_password = driver.find_element(By.XPATH, "//*[@id="'password'"]/div/div[2]/input")
# input_password.send_keys("tandrio373")

time.sleep(5)

driver.close()

print("-----Finish-----")
