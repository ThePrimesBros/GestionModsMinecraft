import requests
from bs4 import BeautifulSoup
import pickle
UNI = requests.get('https://www.minecraftmods.com/')
soup = BeautifulSoup(UNI.text, "lxml")
question = soup.find_all("h2", class_=('post-title'))
print(question)