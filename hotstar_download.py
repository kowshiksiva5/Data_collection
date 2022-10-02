import time
from bs4 import BeautifulSoup as bs
from numpy import empty
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from extract_movies import *

driver_location = '/home/kk/chromedriver_linux64/chromedriver'

def extract_episodes(url):
    name = url.split('/')[5]
    file_name = name + '.txt'
    print('Extracting', name)

    s = Service(driver_location)
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    time.sleep(5)

    scroll(driver)

    soup = bs(driver.page_source, "html.parser")

    a_tags = soup.find("div", {"class": "col-xs-12 content-holder"}).find_all("a")
    for a in a_tags:
        with open('output/'+file_name, "a") as f:
            f.write("https://www.hotstar.com"+a["href"] + "\n")

def extract_episodes_list(url):
    s = Service(driver_location)
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    time.sleep(5)

    scroll(driver)

    soup = bs(driver.page_source, "html.parser")

    a_tags = soup.find("h2", {"class": "tray-title"}).find_all("a")
    for a in a_tags:
        text = a["href"]
        if "episodes" in text:
            return text

def scroll(driver):
        scroll_pause_time = 1 
        screen_height = driver.execute_script("return window.screen.height;")/3
        i = 1
        while True:
            driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
            i += 1
            time.sleep(scroll_pause_time)
            scroll_height = driver.execute_script("return document.body.scrollHeight;")  
            if (screen_height) * i-1 > scroll_height:
                break


def extract(url):
    name = url.split('/')[-1]
    file_name = name + '.txt'
    print('Extracting', name)

    s = Service(driver_location)
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    time.sleep(5)

    scroll(driver)

    soup = bs(driver.page_source, "html.parser")
    a_tags = soup.find("div", {"class": "col-xs-12 content-holder"}).find_all("a")
    for a in a_tags:
        with open(file_name, "a") as f:
            f.write("https://www.hotstar.com"+ a["href"]+'\n')
            # episodes_list = extract_episodes_list("https://www.hotstar.com"+ a["href"])
            # extract_episodes("https://www.hotstar.com"+ episodes_list)



def usefiles(file1):
    with open(file1) as f:
        lines1 = f.readlines()
    lines1 = [line.strip() for line in lines1]
    for i in lines1:
        list = extract_episodes_list(i)
        name = i.split('/')[-1]
        file_name = name + '.txt'
        with open('output/'+file_name, "a") as f:
            print('Extracting', list)
            if list:
                f.write(list + "\n")
            
# languages = ["odia", "hindi", "bengali", "telugu", "malayalam", "tamil", "marathi", "english", "kannada", "korean", "japanese"]
# languages = ["telugu"]

# for i in languages:
# extract("https://www.hotstar.com/in/languages/telugu")
usefiles('seperated.txt')