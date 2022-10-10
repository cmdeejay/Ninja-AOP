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


class NinjaFunctions:
    def __init__(self, email, client_id, first_name, last_name, login_session, status_label):
        self.first_name = first_name.replace("\n", "")
        self.last_name = last_name.replace("\n", "")
        self.client_id = client_id.replace("\n", "")
        self.email = email.replace("/n", "")
        self.session = login_session
        self.status_label = status_label
        self.Url = Urls()

    def idDocuments(self):
        try:
            os.makedirs(self.Url.os_path + self.email)
            self.status_label.config(text="Creating client's folder...\n")
        except OSError:
            tkinter.messagebox.showerror(title='Warning', message='The folder is already exist!')
        self.status_label.config(text="Start downloading...\n")
        url = self.Url.profile_url + self.client_id + "/show?_tab=_12"
        r = self.session.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        src = soup.find_all('img', attrs={'class': 'img-fluid width2'})
        file_format = ["jpg", "pdf", "jpeg", "png", "JPG"]
        try:
            idfront_src = soup.find('img', attrs={'class': 'img-fluid width2'}).get('src')
            for source in src:
                for f in file_format:
                    if f in source.get('src'):
                        file_name = f"{self.Url.os_path_f}/{self.email}/{self.first_name}{self.last_name}{int(time.time())}.{f}"
                        urllib.request.urlretrieve(source.get('src'), file_name)
                        os.startfile(file_name)
            Uti = Utilities()
            new_login_session = Uti.login()
            generate_pdf = new_login_session.get(self.Url.pdfUrl(self.client_id))
            r = new_login_session.get(url)
            soup = BeautifulSoup(r.content, 'html5lib')
            pdf = soup.find('span', attrs={'class': 'gen_pdf'}).find('a')['href']
            self.status_label.config(text="All files download completed...\n")
            return idfront_src, pdf
        except AttributeError:
            self.status_label.config(text="No files uploaded...\n")

    def idTranslation(self):
        Translator = google_translator()
        Data_Generator = Tesseract_Translator()
        try:
            os.makedirs(self.Url.os_path + self.email)
        except OSError:
            tkinter.messagebox.showerror(title='Warning', message='The folder is already exist!')

        format_path = "cot/COT_Format.pdf"
        output_path = self.Url.os_path + self.email + "\\" + self.first_name + self.last_name + "_COT.pdf"
        fillpdfs.get_form_fields(format_path)
        return_data = Data_Generator.formatting()
        form = {'Name and Job Position': 'Charmy Chen, Account Application Officer',
                'Language': 'Chinese and English',
                'ID Type': 'ID',
                'ID Full Name': self.last_name + ' ' + self.first_name,
                'Date of Birth': return_data['DOB'],
                'Expiry Date': return_data['expiry_date'],
                'ID Number': return_data['ID_number'],
                'Document Type': 'ID',
                'Residence Full Name': self.last_name + ' ' + self.first_name,
                'Address': return_data['Address_en'],
                'Issuing Date': return_data['issue_date']}

        fillpdfs.write_fillable_pdf(format_path, output_path, form)
        os.startfile(output_path)

