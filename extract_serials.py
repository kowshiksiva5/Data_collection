import time
from bs4 import BeautifulSoup as bs


def extract_serials(url):
    name = url.split('/')[-1]
    file_name = name + '.txt'
    print('Extracting', name)

    s = Service('/home/west/Downloads/noa/chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    time.sleep(5)

    scroll(driver)

    soup = bs(driver.page_source, "html.parser")
    a_tags = soup.find("div", {"class": "col-xs-12 content-holder"}).find_all("a")
    for a in a_tags:
        with open(file_name, "a") as f:
            f.write("https://www.hotstar.com"+ a["href"]+'\n')
            text = extract_episodes_list("https://www.hotstar.com"+ a["href"])
            extract_episodes("https://www.hotstar.com"+ text)
