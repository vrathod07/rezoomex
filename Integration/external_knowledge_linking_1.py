
'''
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
#import spacy
from re import search
import sys        
 
# appending the directory of spacy
# in the sys.path list
sys.path.append('C:/Users/User/AppData/Local/Programs/Python/Python39/Lib/site-packages')       
# now we can import mod
import spacy  





def init():
      global driver
      options= Options()
      
      
      # chrome 104 location
      options.binary_location = "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"
      options.add_experimental_option("detach", True) # solved error 
      options.add_argument('--no-sandbox')  
      PATH = "D:\\Anika\\VS_code\\PPL\\naturallanguageprocessing\\venv\\Include\\chromedriver.exe"
      driver = webdriver.Chrome(PATH,options=options) 
      



def fetch(job):
    
    all_links=[]
    relevant_links=[]
    ##searchquery=  'https://www.coursera.org/ AND '+'data analyst'+'course'
    searchquery=  'https://www.coursera.org/ AND '+job+' course'
    google_page= driver.get("https://www.google.com/search?q="+searchquery)
    time.sleep(5)
    results = driver.find_elements(by=By.TAG_NAME,value="a");
                                                                 ##print("result =",results)
    for result in results:
                                                                 ##print(result.get_attribute("href")) 
            link= result.get_attribute("href")
            if(link is not None):
                                                                 ## print(type(link))
                                                                ##print(link)
               all_links.append(link)
                                                                 ##print(all_links)
    substring1 = "coursera"
    
   # from all links extracted find the links which have substring "coursera"
    num=0
    for link in all_links:
          
        if(search('https://maps.google.com/maps?q',link)):
                continue 
        if (search(substring1, link)):
                if(link.startswith('https://www.google.com/search?q=')):
                        continue
                elif (link.endswith('enroll')):
                        relevant_links.append(link)
                
                elif(search('professional-certificates',link)):
                        relevant_links.append(link)
                elif(search('specializations',link)):
                        relevant_links.append(link)
                elif(search(job,link)):
                        relevant_links.append(link)
                else:
                        relevant_links.append(link)
                                     
                
                
    print("========================================================")
    print("job=",job)
    #print("Relevant links : ",relevant_links)    #'https://www.coursera.org/professional-certificates/google-data-analytics#enroll',
    newlist= relevant_links
    return newlist




def remove_unwanted_urls(Coursera_links):
    newlist=[]  

    for link in Coursera_links:
                if(link=='https://www.coursera.org/' or search('coursera.org/courseraplus',link)):
                    continue
                if(search('^https://maps.google.com/',link) or search('^https://www.google.com',link) or  search('^https://accounts.google.com',link) or search('search?query=',link) or link.endswith('coursera.org/')):
                    continue
                else:
                    newlist.append(link)
    return newlist



def scrape_skills(job,url):
    mainpage= driver.get(url)
    time.sleep(5)
    print("Landed on coursera course scrape1")
    time.sleep(5)
    print()
    
    items = driver.find_elements(by=By.CLASS_NAME,value="_ontdeqt")
    
    # write to csv file
    if(len(items)>0):
        header = ['designation','skill']
        blankline=['','']
        f = open('Coursera_catalog.csv', 'a',newline='')
        writer = csv.writer(f)
        #writer.writerow(header)
        writer.writerow(blankline)
        f.close()
        
        # skills feed to csv
        for skill in items:
            sk = skill.text
            print(sk)
            row=[job,sk]
            # write a row to the csv file
            f = open('Coursera_catalog.csv', 'a',newline='')
            writer = csv.writer(f)
            writer.writerow(row)

            # close the file
        f.close()

            #<span class="_ontdeqt">Spreadsheet</span>
        
        



def choice_of_links(job,Coursera_links):
    
    empty=[]
    for link in Coursera_links:
        if(search('enroll',link)):
                    return link
                    
        elif(search('professional-certificates',link)):
                    return link
        elif(search('specializations',link)):
                    return link
        elif(search(job,link) or search(job[0:4:1],link) or search('develop',link) or search('software',link)):
            
                    return link
                    
        elif(search('courses?query=',link)):
                    return link
        elif(search('https://www.classcentral',link)):
                Coursera_links.remove(link)
        return link
    


def fetch_different_link(job,url):
    
    print("scrape2")
    all_links=[]
    relevant_links=[]
 
    #link=  'https://www.coursera.org/courses?query=software%20testing'
    link = url
    qpage= driver.get(link)
    source_code=driver.page_source
    

    soup = BeautifulSoup(source_code, 'html.parser')
    div = BeautifulSoup(source_code, 'html.parser').find('div', {'class':'ais-InfiniteHits'})
    #div  = soup.find_all('div',{'class':'ais-InfiniteHits'}) #cds-1 css-0 cds-3 cds-grid-item cds-48 cds-56 cds-68
    
   
    cards_block =div.find_all('li')
    time.sleep(5)
    print("total number of cards on page =",len(cards_block))
   
    #<p class="cds-111 css-z4vnns cds-113"><span class="css-1qajodb"><b>Skills you'll gain: </b></span>Computer Programming, Computer Programming Tools, Java Programming, Mobile Development, Programming Principles, Software, Software Engineering, Software Testing, Unit Testing</p>
    num=1   # extract only first 3 cards
    for tags in cards_block:
        if(num<=3):
          skills =tags.find_all('p')  #  type is <class 'bs4.element.Tag'>
          skills_results = [s.text for s in skills]  # type is string now   
          
          name_of_course= tags.find('h2')   # type is <class 'bs4.element.Tag'>
          name_of_course_results = [i.text for i in name_of_course] #type is string now
          print("num= below ",num)
          print("------------------",skills_results[0]) 
          print("-------------------",name_of_course_results[0])
          skills= extract(skills_results[0])
          feedcsv(skills,job)
          
        else:
              break
        num=num+1
        
       
        
         
def extract(str):
    # input str= " Skills you'll gain: Computer Programming,
    # Computer Programming Tools, Java Programming,
    # Mobile Development, Programming Principles, Software,
    # Software Engineering, Software Testing, Unit Testing   "     extract skills and put in csv
    
    skills= str.split(':') 
    print(skills)
    if(len(skills)>1):
     skills= skills[1].split(',')
   # print(skills)   #[' Computer Programming','Computer Programming Tools',' Java Programming','Mobile Development', ' Programming Principles', ' Software', 'Software Engineering', ' Software Testing', ' Unit Testing']
     return skills
 
 
def feedcsv(skills,job):
        #     skills=  #[' Computer Programming',
#  'Computer Programming Tools',
#  ' Java Programming',
#  'Mobile Development',
#  ' Programming Principles',
#  ' Software',
#  'Software Engineering',
#  ' Software Testing',
#  ' Unit Testing']  , job = 'Software tester'

 # skills feed to csv
   if(skills is not None):
     for skill in skills:
            sk = skill
            print(sk)
            row=[job,sk]
            # write a row to the csv file
            f = open('Coursera_catalog.csv', 'a',newline='')
            writer = csv.writer(f)
            writer.writerow(row)
            
def coursera_scraping():
    
    init()
    df = pd.read_csv("designationcsv.csv")
    print(df.head(5))

    designations= df['Designation'].to_list()
    print(designations)
    for job in designations:
        #https://www.google.com/search?q=
        Coursera_links = fetch(job)
        Coursera_links= remove_unwanted_urls(Coursera_links)
            
        if(len(Coursera_links)>0):
            
            url= choice_of_links(job,Coursera_links)
            print("Chosen link : ",url)
            if(url!=[]):
                if(search('https://www.coursera.org/courses?query',url)):
                    #scrape_skills2(job,url)
                    print("goto scrape 2")
                    fetch_different_link(job,url)
                elif(url.startswith('https://www.coursera.org/courses?query')):
                     print("goto scrape 3")
                     fetch_different_link(job,url)
                else:
                    scrape_skills(job,url)
                time.sleep(5)


'''
