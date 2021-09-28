from bs4 import BeautifulSoup
import requests

inhalt_seite = requests.get('https://www.heise.de/').content
soup = BeautifulSoup(inhalt_seite , 'html.parser')
print(soup)
