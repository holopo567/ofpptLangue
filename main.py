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
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")  # حجم الشاشة الافتراضي
options.add_argument("--no-sandbox")
options.add_argument("--mute-audio")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")


driver = uc.Chrome(options=options)
driver.get("https://app.ofppt-langues.ma/gw/api/saml/init?idp=https://sts.windows.net/dae54ad7-43df-47b7-ae86-4ac13ae567af/")

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
        time.sleep(random.uniform(5, 8))  # النوم لوقت عشوائي بعد النقر
    except Exception as e:
        print(f"Error clicking element with mouse: {e}")

def login(email,password):
    
    send_key('//*[@id="i0116"]',email)
    time.sleep(random.uniform(5, 8))
    click_element_with_mouse('//*[@id="idSIButton9"]')
    send_key('//*[@id="i0118"]',password)
    time.sleep(random.uniform(5, 8))
    click_element_with_mouse('//*[@id="idSIButton9"]')
    click_element_with_mouse('//*[@id="idSIButton9"]')
    time.sleep(random.uniform(10, 20))
 


login('2005090100281@ofppt-edu.ma','G3nT!xR7w$8qL9M')

driver.get("https://app.ofppt-langues.ma/platform/discover")
print("lein mcha")
click_element_with_mouse('//*[@id="VOCABULARY"]/ul/li[1]/a')
click_element_with_mouse('//*[@id="theme-provider"]/div[1]/main/div/div[2]/div/a[2]/div')

# تكرار العملية
while True:
    time.sleep(random.uniform(5, 8))  # النوم لوقت عشوائي
    click_element_with_mouse('//*[@id="theme-provider"]/div[1]/main/div/ul[2]/li[1]/a/div')
    time.sleep(random.uniform(5, 8))  # النوم لوقت عشوائي
    click_element_with_mouse('//*[@id="theme-provider"]/div[1]/main/div/div/div[1]/div/div/button')
    time.sleep(70)  # الانتظار لمدة أطول لتقليد حركة الإنسان
    click_element_with_mouse('//*[@id="theme-provider"]/div[1]/main/div/div[2]/a')
    

# إغلاق المتصفح
driver.quit()
