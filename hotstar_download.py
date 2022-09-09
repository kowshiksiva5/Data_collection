import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

def extract_episodes(url):
    name = url.split('/')[5]
    file_name = name + '.txt'
    print('Extracting', name)

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    scroll(driver)

    soup = bs(driver.page_source, "html.parser")

    a_tags = soup.find("div", {"class": "col-xs-12 content-holder"}).find_all("a")
    for a in a_tags:
        with open(file_name, "a") as f:
            print("https://www.hotstar.com"+a["href"])
            f.write("https://www.hotstar.com"+a["href"] + "\n")

def extract_episodes_list(url):
    driver = webdriver.Chrome()
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
        screen_height = driver.execute_script("return window.screen.height;")/2 
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

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    scroll(driver)

    soup = bs(driver.page_source, "html.parser")
    a_tags = soup.find("div", {"class": "col-xs-12 content-holder"}).find_all("a")
    for a in a_tags:
        with open(file_name, "a") as f:
            text = extract_episodes_list("https://www.hotstar.com"+ a["href"])
            extract_episodes("https://www.hotstar.com"+ text)

# languages = ["odia", "hindi", "bengali", "telugu", "malayalam", "tamil", "marathi", "english", "kannada", "korean", "japanese"]
languages = ["telugu"]

# for i in languages:
extract("https://www.hotstar.com/in/channels/star-maa")