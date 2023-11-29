import json
from bs4 import BeautifulSoup
import requests



url = f"https://habr.com/ru/feed/"  # take the Habr url


def get_data(ur):
    a = []
    req = requests.get(ur)
    soup = BeautifulSoup(req.content, "html.parser")
    href_of_the_article = soup.find_all(class_="tm-title__link")  
    for item in range(0, 4):  # start sorted
        https = f"https://habr.com{href_of_the_article[item].get('href')}"
        a.append(https)  # OMG a lot has been written. WHY GOD?? WHYYY
    for i in a:
        print(a)

get_data(url)
