import requests
from bs4 import BeautifulSoup
import pickle
UNI = requests.get("https://stackoverflow.com/questions/tagged/beautifulsoup")
soup = BeautifulSoup(UNI.text, "lxml")
question = soup.find_all("a", class_='question-hyperlink', limit=10)
vote = soup.find_all("div", class_='vote', limit=10)
rep = soup.find_all("div", class_='answered-accepted', limit=10)



for i in range(10):
    print(question[i].text)
    print(vote[i].strong.text)
    print(rep[i].strong.text)
fichier = open("question.csv", "w")
for i in range(10):
    fichier.write(question[i].text +','+ vote[i].strong.text +','+ rep[i].strong.text+"\n")
fichier.close()