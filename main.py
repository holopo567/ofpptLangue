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
import os





user_data_dir = r"C:\\Users\\moham\\AppData\\Local\\Microsoft\\Edge\\User Data"
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # تشغيل بدون واجهة رسومية
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


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
        # تأكد من أن العنصر جاهز للنقر عليه
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()  # تحريك الماوس ثم النقر
        time.sleep(random.uniform(1, 2))  # النوم لوقت عشوائي بعد النقر
    except Exception as e:
        print(f"Error clicking element with mouse: {e}")

def login(email, password):
    click_element_with_mouse('//*[@id="__next"]/main/section[1]/div/div[2]/div/div[3]/a[1]')

    
    # الانتظار للتأكد من فتح نافذة جديدة
    time.sleep(5)
    
    # التأكد من أن النافذة الجديدة قد فتحت
    WebDriverWait(driver, 60).until(lambda driver: len(driver.window_handles) > 1)
    
    # التبديل إلى النافذة الجديدة
    driver.switch_to.window(driver.window_handles[1])
    
    send_key('//*[@id="i0116"]', email)
    click_element_with_mouse('//*[@id="idSIButton9"]')
    send_key('//*[@id="i0118"]', password)
    click_element_with_mouse('//*[@id="idSIButton9"]')
    click_element_with_mouse('//*[@id="idSIButton9"]')



email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
login(email,password)
print(len(driver.window_handles))
driver.get("https://app.ofppt-langues.ma/platform/discover")
click_element_with_mouse('//*[@id="VOCABULARY"]/ul/li[1]/a')
click_element_with_mouse('//*[@id="theme-provider"]/div[1]/main/div/div[2]/div/a[2]/div')

# تكرار العملية
while True:
    try:
        time.sleep(random.uniform(1, 3))  # النوم لوقت عشوائي
        click_element_with_mouse('//*[@id="theme-provider"]/div[1]/main/div/ul[2]/li[1]/a/div')
        time.sleep(random.uniform(1, 3))  # النوم لوقت عشوائي
        click_element_with_mouse('//*[@id="theme-provider"]/div[1]/main/div/div/div[1]/div/div/button')
        time.sleep(70)  # الانتظار لمدة أطول لتقليد حركة الإنسان
        click_element_with_mouse('//*[@id="theme-provider"]/div[1]/main/div/div[2]/a')
    except Exception as e:
            print(f"error: {e}")
            break

# إغلاق المتصفح
driver.quit()
