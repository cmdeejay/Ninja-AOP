from PIL import Image
import pytesseract
from googletrans import Translator
import re


class Tesseract_Translator:
    def __init__(self):
        self.Translator = Translator()
        pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR/tesseract.exe"
        self.path_1 = "ID/ID_4.jpg"
        self.path_2 = "ID/ID_3.jpg"
        self.path_3 = "ID/ID_5.jpg"
        self.id_back = pytesseract.image_to_string(Image.open(self.path_1), lang='chi_sim').replace(" ", "").replace(".", "")
        self.id_front_zh = pytesseract.image_to_string(Image.open(self.path_2), lang='chi_sim').replace("\n", "").replace(" ", "").strip()
        self.ID_number = pytesseract.image_to_string(Image.open(self.path_3), lang='chi_sim').replace("\n", "").replace(" ", "").strip()
        self.disallowed_char = ", '[]:"
        self.issue_date = None
        self.expiry_date = None
        self.Address_zh = None
        self.Address_en = None
        self.DOB = None

    def _translate_id_back_issue_date(self):
        self.id_back = str(re.findall('\d', self.id_back)).replace(", ", "").replace("'", "")
        self.id_back = self.id_back.replace(" ", "").replace("[", "")
        self.issue_date = self.id_back[:4] + "-" + self.id_back[4:6] + "-" + self.id_back[6:8]

        return self.issue_date

    def _translate_id_back_expiry_date(self):
        self.expiry_date = self.id_back[8:12] + "-" + self.id_back[4:6] + "-" + self.id_back[6:8]

        return self.expiry_date

    def _translate_id_front_address(self):
        self.Address_zh = str(re.findall(r'日(.*?)$', self.id_front_zh)).replace("[", "").replace("]", "")
        if len(self.Address_zh) == 0:
            self.Address_zh = str(re.findall(r'目(.*?)$', self.id_front_zh)).replace("[", "").replace("]", "")
        if len(self.Address_zh) == 0:
            self.Address_zh = str(re.findall(r'晶(.*?)$', self.id_front_zh)).replace("[", "").replace("]", "")
        try:
            self.Address_en = str(self.Translator.translate(text=self.Address_zh, src='zh-cn', dest='en'))
        except TypeError:
            self.Address_en = "Can't recognize it! Please snip the image again! "

        return self.Address_en

    def _translate_id_front_DOB(self):
        self.DOB = "1" + str(re.findall(r'1(.*?)日', self.id_front_zh)).replace("年", "-").replace("月", "-")
        self.DOB = str(self.DOB.replace("第", "-"))
        self.DOB = str(self.DOB.replace(" ", "").replace("'", ""))
        self.DOB = str(self.DOB.replace("[", "").replace("]", ""))
        if self.DOB == '1':
            self.DOB = "1" + str(re.findall(r'1(.*?)晶', self.id_front_zh)).replace("年", "-").replace("月", "-")
            self.DOB = str(self.DOB.replace("第", "-"))
            self.DOB = str(self.DOB.replace(" ", "").replace("'", ""))
            self.DOB = str(self.DOB.replace("[", "").replace("]", ""))
        if self.DOB[:2] != '19':
            self.DOB = "2" + str(re.findall(r'2(.*?)日', self.id_front_zh)).replace("年", "-").replace("月", "-")
            self.DOB = str(self.DOB.replace("第", "-"))
            self.DOB = str(self.DOB.replace(" ", "").replace("'", ""))
            self.DOB = str(self.DOB.replace("[", "").replace("]", ""))
        if self.DOB[:2] == "2":
            self.DOB = "1" + str(re.findall(r'1(.*?)目', self.id_front_zh)).replace("年", "-").replace("月", "-")
            self.DOB = str(self.DOB.replace("第", "-"))
        if self.DOB[:2] == '2':
            self.DOB = "1" + str(re.findall(r'1(.*?)卓', self.id_front_zh)).replace("年", "-").replace("月", "-")
        if self.DOB[:2] == '2':
            self.DOB = "1" + str(re.findall(r'1(.*?)晶', self.id_front_zh)).replace("年", "-").replace("月", "-")
            self.DOB = str(self.DOB.replace(" ", "").replace("'", ""))
            self.DOB = str(self.DOB.replace("[", "").replace("]", ""))

        return self.DOB

    def formatting(self):
        self.issue_date = self._translate_id_back_issue_date()
        self.expiry_date = self._translate_id_back_expiry_date()
        self.Address_en = self._translate_id_front_address()
        self.ID_number = self.ID_number
        self.DOB = self._translate_id_front_DOB()

        for char in self.disallowed_char:
            self.issue_date = self._translate_id_back_issue_date().replace(self.disallowed_char, "").replace('"', '')
            self.expiry_date = self._translate_id_back_expiry_date().replace(self.disallowed_char, "").replace('"', '')
            self.Address_en = self._translate_id_front_address().replace(self.disallowed_char, "").replace('"', '')
            self.DOB = self._translate_id_front_DOB().replace(char, "").replace('"', '')

        self.Address_en = ' '.join(re.findall("text='(.*?)', pronunciation", self.Address_en))

        return_data = {
            'issue_date': self.issue_date,
            'expiry_date': self.expiry_date,
            'Address_en': self.Address_en,
            'ID_number': self.ID_number,
            'DOB': self.DOB
        }

        return return_data
