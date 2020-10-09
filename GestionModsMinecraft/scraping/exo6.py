import json
from bs4 import BeautifulSoup
import requests


URL ='https://www.marmiton.org/recettes/recherche.aspx?aqt=noix-de-saint-jacques-pour-2-personnes&ttlt=30'

r = requests.post(URL)
soup = BeautifulSoup(r.text,("lxml"))
h4 =soup.find_all("h4", {"class" : "recipe-card__title"})
print(h4)





