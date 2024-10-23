from selenium.webdriver.common.by import By

from src.utils.global_function import GlobalFunction

print("-----Start to Open Web-----")

print("1. Open Web Chrome (Has been login)")
driver = GlobalFunction.open_chrome("https://www.tokopedia.com/")

GlobalFunction.delay(5)

print("2. Add Sample 1 Product 'Keyboard'")
input_search_product = driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[1]/div/div/div/input")
input_search_product.send_keys("Keyboard")
GlobalFunction.delay(5)
click_search_product = driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[3]/a[1]")
click_search_product.click()

GlobalFunction.delay(5)

print("3. Choose and Go to Details Sample Product 1")
element_name_product_1 = driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a/div[1]/div[2]/div[1]/span")
name_product_1 = element_name_product_1.text
click_detail_product = driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a")
click_detail_product.click()

GlobalFunction.delay(10)

print(f"4. Add Product {name_product_1} to Bucket")
btn_add_to_bucket = driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[4]/div[1]/button[1]")
btn_add_to_bucket.click()

GlobalFunction.delay(5)

print("5. Close Frame")
btn_close_frame = driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/article/header/button")
btn_close_frame.click()

print("6. Add Sample 2 Product 'Mouse'")
input_search_product = driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[1]/div/div/div/input")
input_search_product.send_keys("Mouse")
GlobalFunction.delay(5)
click_search_product = driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[3]/a[1]")
click_search_product.click()

GlobalFunction.delay(5)

print("7. Choose and Go to Details Sample Product 2")
element_name_product_2 = driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a/div[1]/div[2]/div[1]/span")
name_product_2 = element_name_product_2.text
click_detail_product = driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a")
click_detail_product.click()

GlobalFunction.delay(5)

print(f"8. Add Product {name_product_2} to Bucket")
btn_add_to_bucket = driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[4]/div[1]/button[1]")
btn_add_to_bucket.click()

GlobalFunction.delay(5)

print("9. Check List Bucket")
btn_check_in_bucket = driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/article/div/section/div/button")
btn_check_in_bucket.click()
GlobalFunction.delay(5)
element_name_product_in_bucket_1 = driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/section[1]/span[1]")
name_product_in_bucket_1 = element_name_product_in_bucket_1.get_attribute("title")
print(name_product_in_bucket_1)
# if name_product_in_bucket_1 == name_product_1:
#     print(f">> Product 1 - {name_product_1} in your bucket")
# else:
#     print(">> No product in your bucket")
element_name_product_in_bucket_2 = driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/section[1]/span[1]")
name_product_in_bucket_2 = element_name_product_in_bucket_2.get_attribute("title")
print(name_product_in_bucket_2)
# if name_product_in_bucket_2 == name_product_2:
#     print(f">> Product 2 - {name_product_2} in your bucket")
# else:
#     print(">> No product in your bucket")

print("10. Delete All and Refresh to Home")
btn_delete_list_product = driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/button")
btn_delete_list_product.click()
GlobalFunction.delay(5)
btn_ready_delete = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/button[2]")
btn_ready_delete.click()
GlobalFunction.delay(5)
driver.get("https://www.tokopedia.com/")
driver.refresh()

print("-----Finish-----")
driver.close()
