from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
import tempfile
user_data_dir = tempfile.mkdtemp()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--headless")  # Use new headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# chrome_options.add_argument(r"user-data-dir=C:\Users\gnane\AppData\Local\Google\Chrome\User Data")

# chromedriver_path = r"C:\path\to\chromedriver.exe" 

# service = Service(executable_path=chromedriver_path)

url = "https://portal.spacebasic.com/login"
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

wait = WebDriverWait(driver, 20)

driver.get(url)
password = "23102A010498@"
email = "dinu08642@gmail.com"
time.sleep(3)
# try:
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="chat-bot-widget-close"]'))).click()
#     print("Chat widget closed.")
# except:
#     print("Chat widget close button not found.")
    
# try:
#     wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/aside/div[1]/div[1]/div/div[1]/nav/a[5]'))).click()
#     print("Sign Clicked")
# except:
#     print("Sign Clicked not")
    
    
    


    
   
    


try:
    email_input =wait.until(EC.presence_of_element_located((By.ID, 'email')))
    email_input.click()

    email_input.send_keys(email)
    print("Email entered.")
except Exception as e:
    print("Email input not found:", e)

    
try:
    password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    password_input.send_keys(password)
    print("Password entered.")
except:
    print("Password input not found.")
    
    
# time.sleep(10)
# driver.find_element(By.XPATH, '/html/body/app-root/app-login1/section/div[2]/div/form/button').click()
# time.sleep(9)
# driver.find_element(By.XPATH, '//*[@id="B-4"]/div[1]/span').click()
# time.sleep(9)
# driver.find_element(By.XPATH, '//*[@id="B-4-0"]/div[1]/i').click()
# # //*[@id="B-4"]/div[2]/i


wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-login1/section/div[2]/div/form/button'))).click()
print("Sign Clicked")
try:
    wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))
except:
    print("Spinner not found or already gone.")
try:
    
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="B-4"]/div[1]/span'))).click()
    print("Mess manager Clicked")
except:
    print("Mess manager Not Clicked")
time.sleep(2)
try:
    
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="B-4-0"]/div[1]/i'))).click()
    print("Booking Clicked")
except :
    print("Not Clicked Booking")
try:
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div/div/app-messbookings/section/sbc-custom-tabs/section/div[4]/span'))).click()#tomorrow
    print("Tomorrow Clicked")
except:
    print("Tomorrow Not Clicked")
try:
    label_nv = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div/div/app-messbookings/section/app-transaction/div/table/tbody/tr[2]/td[1]')))
    if label_nv:
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layout-wrapper"]/div/div/app-messbookings/section/app-transaction/div/table/tbody/tr[2]/td[5]/div/button'))).click() ## Button
        print("Non veg booked")
    else:
        print("Non veg booked not found")
        
except Exception as e:
    label_v =  wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div/div/app-messbookings/section/app-transaction/div/table/tbody/tr[1]/td[1]')))
    if label_v:
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layout-wrapper"]/div/div/app-messbookings/section/app-transaction/div/table/tbody/tr[1]/td[5]/div/button'))).click() ## Button
        print("veg booked")
    else:
        print("veg not booked  ")

time.sleep(3)
try:
    
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/ngb-modal-window/div/div/div[3]/div/div[1]/button'))).click()
    print("Booked")
except :
    print("Not booked")

    
