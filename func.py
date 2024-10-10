from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from difflib import SequenceMatcher as ss
from datetime import date, timedelta
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import requests
import random
import time
import os




saving_path_csv = 'THREAD TODAY ARBING/CSV FILES2'
outcome_path_csv = 'THREAD TODAY ARBING/OUCOME FILES'

def main_date(day):
    last_date = date.today() + timedelta(day)
    return last_date


def selenium_init():
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('C:\\Users\\USER\\Desktop\\chrome\\chromedriver.exe', options=options, desired_capabilities=capa)
    wait = WebDriverWait(driver, 60)
    return driver,wait,EC,By



def headless_selenium_init():
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    options = webdriver.ChromeOptions()
    # options.add_argument("user-data-dir=C:\\Users\\USER\\AppData\\Local\\Google\\Chrome")
    options.add_argument('headless')

    driver = webdriver.Chrome('C:\\Users\\USER\\Desktop\\chrome\\chromedriver.exe', options=options, desired_capabilities=capa)
    wait = WebDriverWait(driver, 60)
    return driver,wait,EC,By


def simple_scroll(driver,speed,t_runs,sleep_time=None,scroll_up=None):
    for x in range(t_runs):
        print('SCROLLED',x)
        driver.execute_script(f"scrollBy(0,{speed})")#FOR SCROLLING DOWN/UP
        print('SCROLLED DOWN \n')
        try:
            if scroll_up.lower() == 'yes':
                driver.execute_script(f"scrollBy(0,-{int(speed/2)})")#FOR SCROLLING DOWN/UP
                print('SCROLLED UP \n')
        except:
            pass

        try:
            time.sleep(sleep_time)
        except:
            pass


def selenium_action_init():
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    driver = webdriver.Chrome('C:\\Users\\USER\\Desktop\\chrome\\chromedriver.exe', options=options, desired_capabilities=capa)
    wait = WebDriverWait(driver, 30)
    action = ActionChains(driver=driver)
    return action,driver,wait,EC,By



def save_daily_csv():
    outcome_dir = 'CSV FILES'
    todays_dir = str(main_date(1))+' Files'
    full_path = os.path.join(outcome_dir,todays_dir)
    try:
        os.makedirs(full_path)
    except:
        print('\n PATH ALREADY EXIST BUT WAS CREATED SUCCESFULLY \n')
    return full_path



def requests_init(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,"html.parser")
    tree = html.fromstring(res.content)
    return soup,tree


def requesting_init(url,**kwargs):
    res = requests.get(url)


def bs4_init(url):
    soup = BeautifulSoup(url,'html.parser')
    return soup


def tree_init(optional):
    tree = html.fromstring(optional)


def saving_files(data,path):
    df = pd.DataFrame(data)
    print(df.to_string())

    try:
        df2 = pd.read_csv(path)
        all_df = pd.concat([df2, df], ignore_index=True)
        all_df.to_csv(path, index=False)
        print(' ------------------------------------ ALL FILES SAVED  ------------------------------------- \n \n')

    except:
        df.to_csv(path, index=False)
        print('============================= SECOND FILE SAVED ==========================')



def drop_duplicate(path):
    all_df = pd.read_csv(path)
    all_df = all_df.drop_duplicates(keep='first')
    all_df = all_df.reset_index()
    all_df.drop(['index'], axis=1, inplace=True)
    all_df.to_csv(path, index=False)


def sorting_values(path,value):
    df = pd.read_csv(path)
    df = df.sort_values(by=value,ascending=False)
    df.to_csv(path, index=False)



def scrolling(driver):
    total_page_height = driver.execute_script("return document.body.scrollHeight")
    total_page_height = int(total_page_height) * 3
    browser_window_height = driver.get_window_size(windowHandle='current')['height']
    current_position = driver.execute_script('return window.pageYOffset')

    ap = []
    count = 0
    run = True
    while run:  # total_page_height - current_position > browser_window_height:
        time.sleep(1)
        driver.execute_script(f"window.scrollTo({current_position}, {(browser_window_height + current_position)*1.18} );")
        current_position = driver.execute_script('return window.pageYOffset')
        print(current_position)

        ap.append(current_position)
        count += 1
        if count >= 2:
            if ap[-1] == ap[-2]:
                print('breaking ')
                run = False
