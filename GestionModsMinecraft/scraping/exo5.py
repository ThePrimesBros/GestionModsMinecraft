import json
from bs4 import BeautifulSoup
import requests


def get_definition(x):
    
    URL ='https://www.oxfordlearnersdictionaries.com/definition/english/{0}'.format(x)

    r = requests.get(URL)
    soup = BeautifulSoup(r.text,("lxml"))

    li =soup.find("span", {"class" : "def"})
    return li.text

# ../..


lines = []
with open('vocabulary.txt') as f:
    lines = f.readlines()
    print(lines)

fichier = open("definition.txt", "w")
for i in lines:
    i = i.replace("\n", "")
    i = str(i)
    defi = get_definition(i)
    print(defi)
    fichier.write(i + ' : ' + defi + "\n")
fichier.close()


