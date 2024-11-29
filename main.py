from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


# إعدادات السائق
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--mute-audio")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
    )
    driver = uc.Chrome(options=options)
    return driver


# وظيفة لتسجيل الدخول
def login(driver, email, password):
    try:
        driver.get("https://app.ofppt-langues.ma/gw/api/saml/init?idp=https://sts.windows.net/dae54ad7-43df-47b7-ae86-4ac13ae567af/")
        send_key(driver, '//*[@id="i0116"]', email)
        click_element_with_mouse(driver, '//*[@id="idSIButton9"]')
        send_key(driver, '//*[@id="i0118"]', password)
        click_element_with_mouse(driver, '//*[@id="idSIButton9"]')
        click_element_with_mouse(driver, '//*[@id="idSIButton9"]')
        
    except Exception as e:
        
        print(f"Error in login: {e}")
        
        


# وظيفة لإرسال مفتاح
def send_key(driver, xpath, key):
    try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(key)
    except Exception as e:
        
        print(f"Error in send_key: {e}")


# وظيفة للنقر
def click_element_with_mouse(driver, xpath):
    try:
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
        actions = ActionChains(driver)
        actions.move_to_element(element)
        time.sleep(random.uniform(2, 5))
        actions.click().perform()
        time.sleep(random.uniform(2, 5))
    except Exception as e:
        print(time.time())
        print(f"Error in click_element_with_mouse: {e}")


def click_element_with_css_selector(driver, css_selector):
    try:
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        element.click()
        time.sleep(random.uniform(2, 5))  # تأخير عشوائي لمحاكاة السلوك البشري
    except Exception as e:
        
        print(f"Error in click_element_with_css_selector: {e}")
        



# وظيفة لتجاوز الفيديو

       

def wait_video(driver):
    global  current_time
    try:
        video =  WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#theme-provider > div.c-bUvWKu > main > div > div > div.c-bQzyIt.c-bQzyIt-kqOPqT-alignContent-start.c-bQzyIt-ddIBXx-gap-4 > div > div > div.plyr__video-wrapper > video')))
        time.sleep(random.uniform(2, 5))
        video_duration = driver.execute_script("return arguments[0].duration;", video)
        driver.execute_script("arguments[0].play();", video)
        time.sleep(video_duration+1)
    except Exception as e:
        print(f"Error in wait_video: {e}")
        print("Current Time:", current_time)


    










# الوظيفة الرئيسية
def main():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    driver = setup_driver()
    try:
        print(time.time())
        login(driver, "2005090100281@ofppt-edu.ma", "G3nT!xR7w$8qL9M")
        time.sleep(15)
               
        n=0
        while True:
            
            
            # تحقق من أن الرابط الحالي هو الرابط المطلوب
            if driver.current_url == "https://app.ofppt-langues.ma/platform/discover":
                print("we got the page !")
                click_element_with_css_selector(driver,'#VOCABULARY > ul > li:nth-child(1) > a > p')
                click_element_with_css_selector(driver,'#theme-provider > div.c-bUvWKu > main > div > div:nth-child(3) > div > a:nth-child(1) > div')    
            else:
                print(f"the current page is: {driver.current_url}")
                print("Current Time:", current_time)
                driver.get('https://app.ofppt-langues.ma/gw/api/saml/init?idp=https://sts.windows.net/dae54ad7-43df-47b7-ae86-4ac13ae567af/')
                time.sleep(10)
                driver.get("https://app.ofppt-langues.ma/platform/discover")
                continue


            
            click_element_with_css_selector(driver,'#theme-provider > div.c-bUvWKu > main > div > ul.c-dYOPMy > li:nth-child(1) > a > div')
            click_element_with_css_selector(driver,'#theme-provider > div.c-bUvWKu > main > div > div > div.c-bQzyIt.c-bQzyIt-kqOPqT-alignContent-start.c-bQzyIt-ddIBXx-gap-4 > div > div > button')
            wait_video(driver)
            click_element_with_css_selector(driver,'#theme-provider > div.c-bUvWKu > main > div > div.c-UazGY.c-UazGY-hySSfO-gap-12')
            n+=1
            print(n)


    except Exception as e:
        print("Current Time:", current_time)
        print(f"Error in main loop: {e}")
    finally:
        driver.quit()


# بدء التنفيذ
if __name__ == "__main__":
    main()
