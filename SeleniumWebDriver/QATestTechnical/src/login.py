from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass
import pickle

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

element_input_email = driver.find_element(By.XPATH, "//*[@id='input']")
element_input_email.click()
input_email = driver.find_element(By.XPATH, "//*[@id='input']/div[1]/div[2]/input")
input_email.send_keys("kelvin373.ht@gmail.com")
btn_next = driver.find_element(By.XPATH, "//*[@id='__skipper']/div/div/div/div/main/form/div[3]/button")
btn_next.click()

# input_email = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, "//input[@name='login']"))
# )
# driver.execute_script("arguments[0].focus();", input_email)
# actions = ActionChains(driver)
# actions.move_to_element(input_email).click().perform()
# input_email.send_keys("email123@gmail.com")

time.sleep(5)

print("3. Input Password")
element_input_password = driver.find_element(By.XPATH, "//*[@id='password']")
element_input_password.click()
input_password = driver.find_element(By.XPATH, "//*[@id='password']/div/div[2]/input")
input_password.send_keys("tandrio373")
btn_login = driver.find_element(By.XPATH, "//*[@id='__skipper']/div/div/div/div/main/form/div[4]/button")
btn_login.click()

time.sleep(30)

print("4. Set Cookies")
cookies = driver.get_cookies()

with open("cookies.pkl", "wb") as file:
    pickle.dump(cookies, file)

driver.close()

print("-----Finish-----")
