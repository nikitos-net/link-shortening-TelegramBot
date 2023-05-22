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
    try:
        url = tree.xpath('//span[@class="shortener__short-link-text "]/text()')[0]
        qr_url = tree.xpath('//img[@class="qr-code qr-code_visible"]/@src')[0]
        driver.close()
        return [url, qr_url]
    except BaseException:
        driver.close()
        return []
