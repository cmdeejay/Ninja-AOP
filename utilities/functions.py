from tkinter import messagebox
from google_trans_new import google_translator
from utilities.Translator import Tesseract_Translator
from utilities.ninja_utilities import Utilities
import os
import tkinter
from fillpdf import fillpdfs
from bs4 import BeautifulSoup
import time
import urllib
from restrict.urls import Urls
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import json


class NinjaFunctions:
    def __init__(self, email, client_id, first_name, last_name, login_session, status_label):
        self._first_name = first_name.replace("\n", "")
        self._last_name = last_name.replace("\n", "")
        self._client_id = client_id.replace("\n", "")
        self._email = email.replace("/n", "")
        self._session = login_session
        self._status_label = status_label
        self._Url = Urls()

    def idDocuments(self):
        try:
            os.makedirs(self._Url.os_path + self._email)
            self._status_label.config(text="Creating client's folder...\n")
        except OSError:
            tkinter.messagebox.showerror(title='Warning', message='The folder is already exist!')
        self._status_label.config(text="Start downloading...\n")
        _url = self._Url.profile_url + self._client_id + "/show?_tab=_12"
        _r = self._session.get(_url)
        _soup = BeautifulSoup(_r.content, 'html5lib')
        _src = _soup.find_all('img', attrs={'class': 'img-fluid width2'})
        _file_format = ["jpg", "pdf", "jpeg", "png", "JPG"]
        try:
            _idfront_src = _soup.find('img', attrs={'class': 'img-fluid width2'}).get('src')
            for _source in _src:
                for _f in _file_format:
                    if _f in _source.get('src'):
                        _file_name = f"{self._Url.os_path_f}/{self._email}/{self._first_name}{self._last_name}{int(time.time())}.{f}"
                        urllib.request.urlretrieve(_source.get('src'), _file_name)
                        os.startfile(_file_name)
            _Uti = Utilities()
            _new_login_session = _Uti.login()
            _generate_pdf = _new_login_session.get(self._Url.pdfUrl(self._client_id))
            _new_r = _new_login_session.get(_url)
            _soup = BeautifulSoup(_new_r.content, 'html5lib')
            _pdf = _soup.find('span', attrs={'class': 'gen_pdf'}).find('a')['href']
            self._status_label.config(text="All files download completed...\n")
            return _idfront_src, _pdf
        except AttributeError:
            self._status_label.config(text="No files uploaded...\n")

    def idTranslation(self):
        _Translator = google_translator()
        _Data_Generator = Tesseract_Translator()
        try:
            os.makedirs(self._Url.os_path + self._email)
        except OSError:
            tkinter.messagebox.showerror(title='Warning', message='The folder is already exist!')

        _format_path = "cot/COT_Format.pdf"
        _output_path = self._Url.os_path + self._email + "\\" + self._first_name + self._last_name + "_COT.pdf"
        fillpdfs.get_form_fields(_format_path)
        _return_data = _Data_Generator.formatting()
        _form = {'Name and Job Position': 'Charmy Chen, Account Application Officer',
                 'Language': 'Chinese and English',
                 'ID Type': 'ID',
                 'ID Full Name': self._last_name + ' ' + self._first_name,
                 'Date of Birth': _return_data['DOB'],
                 'Expiry Date': _return_data['expiry_date'],
                 'ID Number': _return_data['ID_number'],
                 'Document Type': 'ID',
                 'Residence Full Name': self._last_name + ' ' + self._first_name,
                 'Address': _return_data['Address_en'],
                 'Issuing Date': _return_data['issue_date']}

        fillpdfs.write_fillable_pdf(_format_path, _output_path, _form)
        os.startfile(_output_path)

    def bo_check(self):
        _ser = Service('driver/chromedriver.exe')
        _normal_driver_option = webdriver.ChromeOptions()
        _normal_driver_option.add_experimental_option("detach", True)
        _normal_driver_option.add_experimental_option('excludeSwitches', ['enable-logging'])
        _driver = webdriver.Chrome(service=_ser, options=_normal_driver_option)
        _driver.maximize_window()
        _bo_url = Urls.profile_url + self._client_id + "/show"
        _driver.get(_bo_url)
        with open('restrict/bo_credentials.json', 'r') as fp:
            _login_data = json.load(fp)
        _username = _driver.find_element(By.NAME, "admin_username")
        _username.send_keys(_login_data["admin_username"])
        password = _driver.find_element(By.NAME, "admin_password")
        password.send_keys(_login_data["admin_password"])
        _driver.find_element(By.CLASS_NAME, "col-xs-4").click()
