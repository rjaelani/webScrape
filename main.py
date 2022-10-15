from bs4 import BeautifulSoup
import requests


page = requests.get("https://www.pikiran-rakyat.com/")
soup = BeautifulSoup(page.content, 'html.parser')

item = soup.find_all('div', class_='most__item')

print(item)