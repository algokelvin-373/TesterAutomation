from src.utils.global_function import GlobalFunction
from success_increase_decrease_item_product import SuccessInCreaseDecreaseItemProduct
from success_add_one_product_in_bucket import SuccessAddOneProductInBucket
from success_add_more_than_one_product_in_bucket import SuccessAddMoreThanOneProductInBucket
from success_add_one_product_more_than_one_items_in_bucket import SuccessAddOneProductMoreThanOneItemInBucket
from success_add_more_than_one_product_more_than_one_items_in_bucket import SuccessAddMoreThanOneProductMoreThanOneItemsInBuckets

if __name__ == '__main__':
    # Scenario 1
    print("Skenario 1: Sukses Menambah dan Mengurangi Item Pada Tiap Product di Keranjang. \t\t\t [PROSES TESTING]")
    search_product = "Indomie"
    scenario_positive_1 = SuccessInCreaseDecreaseItemProduct()
    print(f"Skenario 1: Sukses Menambah dan Mengurangi Item Pada Tiap Product di Keranjang. \t\t\t [HASIL: {scenario_positive_1.main(search_product)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 2
    print("Skenario 2: Sukses Input Satu Product ke Keranjang. \t\t\t [PROSES TESTING]")
    search_product = "Indomie"
    scenario_positive_2 = SuccessAddOneProductInBucket()
    print(f"Skenario 2: Sukses Input Product ke Keranjang. \t\t\t [HASIL: {scenario_positive_2.main(search_product)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 3
    print("Skenario 3: Sukses Input Lebih dari satu Product ke Keranjang. \t\t\t [PROSES TESTING]")
    list_search_product = {"Indomie", "Mie Sedap"}
    scenario_positive_3 = SuccessAddMoreThanOneProductInBucket()
    print(f"Skenario 3: Sukses Input Lebih dari satu Product ke Keranjang. \t\t\t [HASIL: {scenario_positive_3.main(list_search_product)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 4
    print("Skenario 4: Sukses Input Lebih dari satu Product ke Keranjang. \t\t\t [PROSES TESTING]")
    search_product = "Indomie"
    total_item = 5
    scenario_positive_4 = SuccessAddOneProductMoreThanOneItemInBucket()
    print(f"Skenario 4: Sukses Input Lebih dari satu Product ke Keranjang. \t\t\t [HASIL: {scenario_positive_4.main(search_product, total_item)}]")
    GlobalFunction.delay(5)

    print("\n\n")

    # Scenario 5
    print("Skenario 5: Sukses Input Lebih dari satu Product ke Keranjang yang dimana tiap product lebih dari satu item. \t\t\t [PROSES TESTING]")
    list_search_product = {"Indomie", "Mie Sedap"}
    scenario_positive_5 = SuccessAddMoreThanOneProductMoreThanOneItemsInBuckets()
    print(f"Skenario 5: Sukses Input Lebih dari satu Product ke Keranjang yang dimana tiap product lebih dari satu item. \t\t\t [HASIL: {scenario_positive_5.main(list_search_product)}]")
    GlobalFunction.delay(5)
