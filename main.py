from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import random



user_data_dir = r"C:\\Users\\moham\\AppData\\Local\\Microsoft\\Edge\\User Data"
options = webdriver.ChromeOptions()
#options.add_argument(f"--user-data-dir={user_data_dir}")

driver = uc.Chrome(options=options)
driver.get("https://app.ofppt-langues.ma/platform/discover")

def send_key(xpath,key):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.send_keys(key)
        
    except Exception as e:
        print(f"Error clicking element with mouse: {e}")

def click_element_with_mouse(xpath):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()  # تحريك الماوس ثم النقر
        time.sleep(random.uniform(1, 2))  # النوم لوقت عشوائي بعد النقر
    except Exception as e:
        print(f"Error clicking element with mouse: {e}")

def login(email,password):
    click_element_with_mouse('//*[@id="__next"]/main/section[1]/div/div[2]/div/div[3]/a[1]')
    driver.switch_to.window(driver.window_handles[1])
    send_key('//*[@id="i0116"]',email)
    click_element_with_mouse('//*[@id="idSIButton9"]')
    send_key('//*[@id="i0118"]',password)
    click_element_with_mouse('//*[@id="idSIButton9"]')
    click_element_with_mouse('//*[@id="idSIButton9"]')
    time.sleep(random.uniform(1, 3))


login('2005090100281@ofppt-edu.ma','G3nT!xR7w$8qL9M')
driver.get("https://app.ofppt-langues.ma/platform/discover")
click_element_with_mouse('//*[@id="VOCABULARY"]/ul/li[1]/a')
click_element_with_mouse('//*[@id="theme-provider"]/div[1]/main/div/div[2]/div/a[2]/div')

# تكرار العملية
while True:
    time.sleep(random.uniform(1, 3))  # النوم لوقت عشوائي
    click_element_with_mouse('//*[@id="theme-provider"]/div[1]/main/div/ul[2]/li[1]/a/div')
    time.sleep(random.uniform(1, 3))  # النوم لوقت عشوائي
    click_element_with_mouse('//*[@id="theme-provider"]/div[1]/main/div/div/div[1]/div/div/button')
    time.sleep(70)  # الانتظار لمدة أطول لتقليد حركة الإنسان
    click_element_with_mouse('//*[@id="theme-provider"]/div[1]/main/div/div[2]/a')

# إغلاق المتصفح
driver.quit()