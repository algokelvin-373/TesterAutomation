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

print("4. Add Product to Bucket")
btn_add_to_bucket = driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[4]/div[1]/button[1]")
btn_add_to_bucket.click()

GlobalFunction.delay(5)

print("5. Check List Bucket")
btn_check_in_bucket = driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/article/div/section/div/button")
btn_check_in_bucket.click()
GlobalFunction.delay(2)
element_name_product_in_bucket = driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/section[1]/span[1]/a")
name_product_in_bucket = element_name_product_in_bucket.text
if name_product_in_bucket == name_product:
    print(f">> {name_product} in your bucket")
else:
    print(">> No product in your bucket")

GlobalFunction.delay(5)

print("6. Delete all and refresh to Main Home")
btn_delete_list_product = driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/button")
btn_delete_list_product.click()
GlobalFunction.delay(5)
btn_ready_delete = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/button[2]")
btn_ready_delete.click()
GlobalFunction.delay(5)
driver.get("https://www.tokopedia.com/")
driver.refresh()

GlobalFunction.delay(5)

print("-----Finish-----")
driver.close()
