import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Lokasi folder profil Chrome (ganti sesuai dengan OS dan profil Anda)
user_profile = "user-data-dir=C:/Users/kelvi/AppData/Local/Google/Chrome/User Data"

# Set opsi untuk menggunakan profil Chrome yang sedang aktif
options = Options()
options.add_argument(user_profile)
# options.add_argument("--headless")  # Tambahkan argumen untuk mode headless
# options.add_argument("--disable-gpu")  # Diperlukan pada beberapa sistem

# Buat instance driver dengan opsi tersebut
driver = webdriver.Chrome(options=options)

# Lakukan tindakan seperti biasa
driver.get("https://www.tokopedia.com/")

time.sleep(30)

# Tutup browser setelah selesai
driver.close()
