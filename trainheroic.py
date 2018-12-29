#%%
from decouple import config, Csv
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

U_NAME = config('U_NAME')
U_PASS = config('U_PASS')

#%%
opts = Options()
opts.set_headless()
assert opts.headless
browser = Chrome(options=opts)


#%%
def withdrawTrial(file):
    browser.get('http://admin.trainheroic.com/login')
    # browser.get_screenshot_as_file('login.png')
    
    login = browser.find_element_by_name('email')
    passw = browser.find_element_by_name('password')
    login.send_keys(U_NAME)
    passw.send_keys(U_PASS)
    browser.find_element_by_id('loginButton').click()
    time.sleep(10)
    browser.get_screenshot_as_file('loginSuccess.png')
    data = pd.read_csv(file)['Email Address']
    for email in data:
        print(email)
        browser.find_element_by_id('nav-users').click()
        time.sleep(5)
        # browser.get_screenshot_as_file('users.png')
        searchField = browser.find_element_by_id('pageSearch')
        searchField.send_keys(email)
        searchField.send_keys(Keys.RETURN)
        time.sleep(5)
        browser.get_screenshot_as_file('build/userdetail.png')
        try:
            browser.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[4]').click() # Get list
        except:
            continue
        time.sleep(5)
        try:
            trialbox = browser.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/div[6]/input')
        except:
            continue
        trialbox.click() if trialbox.is_selected() else None
    browser.close()

#%%   
file = '~/Downloads/Documents/closeAccountAutomation.csv'
withdrawTrial(file)


#%%
# browser.close()


