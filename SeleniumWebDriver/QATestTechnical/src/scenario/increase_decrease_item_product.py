import time

from selenium.webdriver.common.by import By

from src.utils.global_function import GlobalFunction

print("-----Start to Open Web-----")

print("1. Open Web Chrome (Has been login)")
driver = GlobalFunction.open_chrome("https://www.tokopedia.com/")

GlobalFunction.delay(5)

print("2. Add Sample Product 'Keyboard'")
input_search_product = driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[1]/div/div/div/input")
input_search_product.send_keys("Keyboard")
GlobalFunction.delay(2)
click_search_product = driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[3]/a[1]")
click_search_product.click()

GlobalFunction.delay(5)

print("3. Choose and Go to Details Product")
element_name_product = driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a/div[1]/div[2]/div[1]/span")
name_product = element_name_product.text
click_detail_product = driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a")
click_detail_product.click()

GlobalFunction.delay(5)

print(f"4. Increase Item for Product {name_product}")
btn_increase_product = driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[1]/div/button[2]")
total_item_product = 5
for item in range(total_item_product - 1):
    btn_increase_product.click()

GlobalFunction.delay(2)

print(f"5. Decrease Item for Product {name_product}")
btn_adding_product = driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[1]/div/button[2]")
total_item_product = 5
for item in range(total_item_product - 1):
    btn_adding_product.click()

GlobalFunction.delay(2)
