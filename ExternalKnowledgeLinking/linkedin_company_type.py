



import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver 
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import time
import csv  
import pandas as pd


import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



def init():
    options= Options()
    options.binary_location = "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"
    options.add_experimental_option("detach", True) # solved error 
    options.add_argument('--no-sandbox')
    
      # for chrome version 104 put local path 
    PATH = "D:\\Anika\\VS_code\\PPL\\naturallanguageprocessing\\venv\\Include\\chromedriver.exe"
    global driver
    #driver = webdriver.Chrome(PATH,options=options) 
    driver = webdriver.Chrome(PATH,service=Service(ChromeDriverManager().install()),options=options) 
    
    driver.get("https://www.linkedin.com")

    username = driver.find_element(by=By.CLASS_NAME,value='input__input')
    time.sleep(2)
    # dummy account email and password
    username.send_keys('ganax45994@otodir.com')
    password = driver.find_element(by=By.ID,value='session_password')
    time.sleep(5)
    password.send_keys('kimkim12345') 

    log_in_button = driver.find_element(by=By.CLASS_NAME,value='sign-in-form__submit-button') 
    log_in_button.click()
    time.sleep(5)
    
    find_on_linkedin()
    
    
    
    
def find_on_linkedin():
       
        #read input company from given lst file (companycsv) and scrape in loop
    with open('companycsv.csv', 'r') as file:
        reader = csv.reader(file)
        num=0
        for row in reader:
            if(num==0):
                num=num+1   
                continue  # skip first titles row
            else:
                print(row)
                company=row[0]  # first element of list , list is like = ['Suven Consultant Pvt ltd']
                # to get card_link = "https://www.linkedin.com/company/amazon"
                
                try:
                
                    driver.get(f"https://www.linkedin.com/company/{company}")
                    time.sleep(10)

                    tag = driver.find_element(by=By.CLASS_NAME,value="org-top-card-summary-info-list__info-item")
                    description= tag.text
                    data = [company,description]
                
                    
                    print(data)
                    print("-------")
                    
                    # writing in file => output file
                    with open('company1.csv', 'a', encoding='UTF8') as f:
                        # write the data
                        writer = csv.writer(f)
                        writer.writerow(data)
                    num=num+1
                    
                except NoSuchElementException:  #company name does not exist on linkedin
                    #print("invalid ")
                    num=num+1  
                    
def main():
    init()
    
main()