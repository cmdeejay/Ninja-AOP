import requests
from urllib.request import urlopen
from restrict.urls import Urls
import json
from bs4 import BeautifulSoup
import re


class Utilities:
    def __init__(self):
        self._url = Urls()
        self.s = requests.Session()
        self._search_url = None

    def login(self):
        with open('restrict/bo_credentials.json', 'r') as fp:
            _login_data = json.load(fp)
        self.s.post(self._url.login_url, data=_login_data)
        return self.s

    def scrapId(self, trading_login):
        self._search_url = self._url.tradingSearch(trading_login)
        _response = self.login().get(self._search_url)
        _soup = BeautifulSoup(_response.content, "html5lib")
        _href = _soup.find('td', attrs={'class': 'sonata-ba-list-field sonata-ba-list-field-orm_one_to_one'}).find('a')['href']
        client_id = str(re.findall(r'profile/(.*?)/show', _href)).replace("[", "").replace("]", "")
        client_id = client_id.replace("'", "")
        return client_id

    def scrapEmail(self, trading_id):
        self._search_url = self._url.tradingSearch(trading_id)
        response = self.login().get(self._search_url)
        soup = BeautifulSoup(response.content, "html5lib")
        email = soup.find('td', attrs={'class': 'sonata-ba-list-field sonata-ba-list-field-orm_one_to_one'}).find('a').text
        return email
