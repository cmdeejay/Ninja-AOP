from utilities.ninja_utilities import Utilities
from restrict.urls import Urls
from bs4 import BeautifulSoup
import requests
import cv2
from urllib.request import urlopen
import numpy as np
from utilities.teams_webhook import webhook_class_result, webhook_not_found


def classify(accounts):
    Uti = Utilities()
    categories = ["Chinese ID FRONT", "Chinese ID BACK", 'Not Chinese ID']
    for account in accounts:
        try:
            client_id = Uti.scrapId(trading_login=str(account[0]))
        except AttributeError:
            webhook_not_found(account[0])
            continue
        url_profile = f"{Urls.profile_url}{client_id}/show"
        r = Uti.login().get(url_profile)
        soup = BeautifulSoup(r.content, 'html5lib')
        src = soup.find_all('img', attrs={'class': 'img-fluid width2'})
        filetype = ['jpg', 'jpeg', 'png', 'JPG']
        predictions = []
        idfront_src = ''
        try:
            idfront_src = soup.find('img', attrs={'class': 'img-fluid width2'}).get('src')
            for source in src:
                for f in filetype:
                    if f in source.get('src'):
                        X = prepare(source.get('src'))
                        response = requests.post(Urls.ml_api_url, json={'ima': X})
                        prediction = response.json()['prediction']
                        predictions.append(prediction)
        except AttributeError as e:
            pass
        webhook_class_result(account[0], predictions, url_profile, idfront_src)


def prepare(path):
    resp = urlopen(path)
    img_array = np.asarray(bytearray(resp.read()), dtype="uint8")
    img_size = 80
    img_array = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (img_size, img_size))
    return new_array.reshape(-1, img_size, img_size, 1).tolist()
