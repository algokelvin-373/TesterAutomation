from selenium.webdriver.common.by import By

from src.utils.global_function import GlobalFunction


class SuccessInCreaseDecreaseItemProduct:
    def __init__(self):
        self.__name_product = ""

        print("1. Open Web Chrome (Has been login)")
        self.__driver = GlobalFunction.open_chrome("https://www.tokopedia.com/")
        GlobalFunction.delay(5)

    def main(self, search_data):
        self.add_product(search_data)
        GlobalFunction.delay(5)

        self.go_to_detail_product()
        GlobalFunction.delay(5)

        self.increase_item_product()
        GlobalFunction.delay(5)

        self.decrease_item_product()
        GlobalFunction.delay(5)

        return self.close_web()

    def add_product(self, search_data):
        print(f"2. Add Sample Product from Result Search '{search_data}'")
        input_search_product = self.__driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[1]/div/div/div/input")
        input_search_product.send_keys(search_data)
        GlobalFunction.delay(5)
        click_search_product = self.__driver.find_element(By.XPATH, "//*[@id='header-main-wrapper']/div[2]/div[2]/div[3]/a[1]")
        click_search_product.click()

    def go_to_detail_product(self):
        print("3. Choose and Go to Details Product")
        element_name_product = self.__driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a/div[1]/div[2]/div[1]/span")
        self.__name_product = element_name_product.text
        click_detail_product = self.__driver.find_element(By.XPATH, "//*[@id='zeus-root']/div/div[2]/div/div[2]/div[4]/div[1]/div[7]/a")
        click_detail_product.click()

    def increase_item_product(self):
        print(f"4. Increase Item for Product {self.__name_product}")
        btn_increase_product = self.__driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[1]/div/button[2]")
        total_item_product = 10
        for item in range(total_item_product - 1):
            btn_increase_product.click()

    def decrease_item_product(self):
        print(f"5. Decrease Item for Product {self.__name_product}")
        btn_adding_product = self.__driver.find_element(By.XPATH, "//*[@id='pdpFloatingActions']/div[1]/div/button[1]")
        total_item_product = 10
        for item in range(total_item_product - 1):
            btn_adding_product.click()

    def close_web(self):
        print("6. Finish")
        self.__driver.close()
        return "VALID"