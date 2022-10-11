import requests
from urllib.request import urlopen
from restrict.urls import Urls
import json
from bs4 import BeautifulSoup
import re


class Utilities:
    def __init__(self):
        self.url = Urls()
        self.s = requests.Session()
        self.login_url = self.url.login_url
        self.search_url = None

    def login(self):
        with open('restrict/bo_credentials.json', 'r') as fp:
            login_data = json.load(fp)
        self.s.post(self.login_url, data=login_data)
        return self.s

    def scrapId(self, trading_login):
        self.search_url = self.url.tradingSearch(trading_login)
        response = self.login().get(self.search_url)
        soup = BeautifulSoup(response.content, "html5lib")
        href = soup.find('td', attrs={'class': 'sonata-ba-list-field sonata-ba-list-field-orm_one_to_one'}).find('a')['href']
        client_id = str(re.findall(r'profile/(.*?)/show', href)).replace("[", "").replace("]", "")
        client_id = client_id.replace("'", "")
        return client_id

    def scrapEmail(self, trading_id):
        self.search_url = self.url.tradingSearch(trading_id)
        response = self.login().get(self.search_url)
        soup = BeautifulSoup(response.content, "html5lib")
        email = soup.find('td', attrs={'class': 'sonata-ba-list-field sonata-ba-list-field-orm_one_to_one'}).find('a').text
        return email
