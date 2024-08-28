import requests
from bs4 import BeautifulSoup
from datetime import datetime
import lxml 

url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='

today = datetime.today().strftime('%d/%m/%Y')
url = url + str(today)

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

def get_course(id):
    return soup.find('valute', {'id': id}).value.text





