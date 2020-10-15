import requests
import json
from bs4 import BeautifulSoup
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
import re
import sys
from mods.models import Mods


MATCH_ALL = r'.*'

URL = "https://www.minecraftmods.com/"
#headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKhttps://www.minecraftmods.com/page/2/37.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36' }


#browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')https://www.minecraftmods.com/page/2/
#browser.get(URL)
#time.sleep(1)
#print(browser.title)
#time.sleep(1)
#browser.quit()

def like(string):
    """
    Return a compiled regular expression that matches the given
    string with any prefix and postfix, e.g. if string = "hello",
    the returned regex matches r".*hello.*"
    """
    string_ = string
    if not isinstance(string_, str):
        string_ = str(string_)
    regex = MATCH_ALL + re.escape(string_) + MATCH_ALL
    return re.compile(regex, flags=re.DOTALL)


def find_by_text(soup, text, tag, **kwargs):
    """
    Find the tag in soup that matches all provided kwargs, and contains the
    text.

    If no match is found, return None.
    If more than one match is found, raise ValueError.
    """
    elements = soup.find_all(tag, **kwargs)
    matches = []
    for element in elements:
        if element.find(text=like(text)):
            matches.append(element)
    if len(matches) > 1:
        raise ValueError("Too many matches:\n" + "\n".join(matches))
    elif len(matches) == 0:
        return None
    else:
        return matches[0]

def scrap(nbPage):
    r = requests.get(URL)
    scrapPage(r)
    if nbPage > 1 :      
        for i in range(2,nbPage):
            r2 = requests.get(URL+"page/"+str(i)+"/")
            scrapPage(r2)

def scrapPage(request):
    soup = BeautifulSoup(request.text,"lxml")
    #print(soup.prettify())
    blogRow = soup.find("section", {"class" : 'main-content'})
    childrenArticles = blogRow.findChildren("article")
    for child in childrenArticles:
        a = child.find("a", {"class" : 'transition'})
        print('Lien image:')
        print(a.img['src'])
        h2 = child.find("h2", {"class" : 'post-title'})
        print('Lien page:')
        print(h2.a['href'])
        linkPage = h2.a['href']
        print('Titre:')
        print(h2.text)
        divdesc = child.find("div", {"class" : 'post-content'})
        print('Description:')
        print(divdesc.text)
        divcreaver = child.find("div", {"class" : 'post-meta'})
        divver = divcreaver.find("span", {"class" : 'version'})
        print('Version:')
        print(divver.text)
        divcrea = divcreaver.find("span", {"class" : 'developer'})
        print('Creator:')
        print(divcrea.text)
        print('//////////////////////////////////////////////')
        r2 = requests.get(linkPage.replace(' ',''))
        soup2 = BeautifulSoup(r2.text,"lxml")   
        divdownload = find_by_text(soup2, 'Download', 'a')
        if divdownload['href'] != 'Nonetype':
            linkDownload = divdownload['href']
        else: 
            linkDownload =''
        print('Lien download:')
        print(linkDownload)
        print('//////////////////////////////////////////////')
           

scrap(40)







    