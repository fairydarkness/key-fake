import re
import keyboard
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pyperclip


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.page_load_strategy = 'none'
options.add_argument("--start-maximized")
options.add_argument("--lang=ru-RU")
options.add_argument("Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")

service = Service(executable_path="путь к хром-драйверу")
driver = uc.Chrome(service=service,options=options)

driver.get("https://store.steampowered.com/account/registerkey")

print("Ожидаю нажатие Alt+P для продолжения...")
keyboard.wait('alt+p')

passte = pyperclip.paste()
key = re.findall(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789]{5}[-]{1}[ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789]{5}[-]{1}[ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789]{5})', passte)
print("Ключ - ", key)

key_field = driver.find_element(By.ID, "product_key")
key_field.send_keys(key)

checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
checkbox.click()

ctn = driver.find_element(By.ID, "register_btn")
ctn.click()

input()

driver.quit()


