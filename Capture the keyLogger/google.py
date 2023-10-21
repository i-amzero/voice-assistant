from googlesearch import search
import requests
from bs4 import BeautifulSoup as bs1
import time


query = input("Search : ")

for url in search(query,num_results=2,sleep_interval=2):
    response = requests.get(url)
    time.sleep(1.5)
    getHTML = response.text
    time.sleep(1.5)
    soup = bs1(getHTML,'html.parser')
    time.sleep(1.5)
    for link in soup.find_all("a"):
        print(link)
        print(link.get("href"))


# re = requests.get('https://en.wikipedia.org/wiki/Jason_Momoa')
# print(re.text)