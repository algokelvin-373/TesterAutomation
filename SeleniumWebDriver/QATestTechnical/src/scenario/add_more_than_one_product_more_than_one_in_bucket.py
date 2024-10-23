from selenium.webdriver.common.by import By

from src.utils.global_function import GlobalFunction

print("-----Start to Open Web-----")

print("1. Open Web Chrome (Has been login)")
driver = GlobalFunction.open_chrome("https://www.tokopedia.com/")

GlobalFunction.delay(5)

print("2. Add Sample Product 1 'Keyboard'")
input_search_product = driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[1]/div/div/div/input")
input_search_product.send_keys("Keyboard")
GlobalFunction.delay(10)
click_search_product = driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[3]/a[1]")
click_search_product.click()

GlobalFunction.delay(5)

print("3. Choose and Go to Details Product 1")
element_name_product = driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a/div[1]/div[2]/div[1]/span")
name_product_1 = element_name_product.text
click_detail_product = driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a")
click_detail_product.click()

GlobalFunction.delay(5)

print(f"4. Set 3 Item for Product {name_product_1}")
btn_adding_product = driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[1]/div/button[2]")
total_item_product_1 = 3
for item in range(total_item_product_1 - 1):
    btn_adding_product.click()

GlobalFunction.delay(5)

print(f"5. Add Product {name_product_1} to Bucket")
btn_add_to_bucket = driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[4]/div[1]/button[1]")
btn_add_to_bucket.click()

GlobalFunction.delay(5)

print("6. Close Frame")
btn_close_frame = driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/article/header/button")
btn_close_frame.click()

GlobalFunction.delay(5)

print("7. Add Sample 2 Product 'Mouse'")
input_search_product = driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[1]/div/div/div/input")
input_search_product.send_keys("Mouse")
GlobalFunction.delay(5)
click_search_product = driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[3]/a[1]")
click_search_product.click()

GlobalFunction.delay(5)

print("8. Choose and Go to Details Sample Product 2")
element_name_product_2 = driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a/div[1]/div[2]/div[1]/span")
name_product_2 = element_name_product_2.text
click_detail_product = driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a")
click_detail_product.click()

GlobalFunction.delay(5)

print(f"9. Set 2 Item for Product {name_product_2}")
btn_adding_product = driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[1]/div/button[2]")
total_item_product_2 = 2
for item in range(total_item_product_2 - 1):
    btn_adding_product.click()

GlobalFunction.delay(5)

print(f"10. Add Product {name_product_2} to Bucket")
btn_add_to_bucket = driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[4]/div[1]/button[1]")
btn_add_to_bucket.click()

GlobalFunction.delay(5)

print("11. Check List Bucket")
btn_check_in_bucket = driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/article/div/section/div/button")
btn_check_in_bucket.click()
GlobalFunction.delay(5)
element_name_product_in_bucket = driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/section[1]/span[1]/a")
name_product_in_bucket = element_name_product_in_bucket.text
print(name_product_in_bucket)
# if name_product_in_bucket == name_product:
#     print(f">> Product '{name_product}' in your bucket [MATCH]")
element_total_item_product_in_bucket = driver.find_element(By.XPATH, "//*[@id='__skipper']/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/input")
total_item_product_in_bucket = element_total_item_product_in_bucket.get_attribute("value")
print(total_item_product_in_bucket)
# if int(total_item_product_in_bucket) == total_item_product:
#     print(f">> Total Item: {total_item_product} [MATCH]")

print("12. Delete All and Refresh to Home Page")
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
