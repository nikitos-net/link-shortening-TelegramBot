import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from lxml import html
def get_cut_url(url):
    
    driver = webdriver.Chrome()

    URL_TEMPLATE = "https://api.glebins.ru/links/"
    driver.get(URL_TEMPLATE)

    element = driver.find_element("xpath", "//input[@id='get_url']")
    element.send_keys(url)

    option = driver.find_element("xpath", "//button[@id='send']")
    option.click()

    URL_TEMPLATE = driver.current_url

    r = requests.get(URL_TEMPLATE)
    tree = html.fromstring(r.text)

    url = tree.xpath('//a[@id="result_url"]/text()')[0]
    driver.close()
    return url

