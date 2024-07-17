from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

kktix_url="https://kktix.com/events/3d85405d/registrations/new"
line_token='NGgWRIyugcoa06rkteTTS32nzfmrUQh5BgqbQDYzI1R'
line_api='https://notify-api.line.me/api/notify'

#browser
driver = webdriver.Chrome()
driver.get(kktix_url)
    
def login():
    driver.find_element(By.XPATH, '//*[@id="guestModal"]/div[2]/div/div[3]/a[2]').click() #login button
    #enter email
    email = driver.find_element(By.XPATH, '//*[@id="user_login"]') 
    email.clear()
    email.send_keys("yourEmail")
    #enter password
    pwd=driver.find_element(By.XPATH, '//*[@id="user_password"]') 
    pwd.clear()
    pwd.send_keys('yourPassword')
    # click login
    driver.find_element(By.XPATH, '//*[@id="new_user"]/input[3]').click() #login button

def ticket():
    while 1:
        try:
            wait = WebDriverWait(driver, 1)
            ticket_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ticket_755071"]/div/span[3]/button[2]'))) #add ticket button
            ticket_button.click()
            break
        except:
            driver.refresh()
            sleep(0.5)

def line_notify(msg):
    headers = {'Authorization': 'Bearer ' + line_token}
    data = {'message': msg}
    requests.post(line_api, headers=headers, data=data)

login()
ticket()

# click person_agree
driver.find_element(By.XPATH, '//*[@id="person_agree_terms"]').click() 

# click next
driver.find_element(By.XPATH, '//*[@id="registrationsNewApp"]/div/div[5]/div[4]/button/span').click() 

# notify
line_notify('買票!!!!!!!!!!')

sleep(50)



'''
#立即購票
driver.find_element(By.XPATH, '//*[@id="order-now"]/a').click()

#loginCookies
driver.delete_all_cookies()
driver.add_cookie({"name": "locale", "value": "zh-TW"})
driver.refresh()
'''