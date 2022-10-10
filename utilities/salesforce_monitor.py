import pandas as pd
import selenium.common.exceptions as exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime
import pyttsx3
import io
import winsound
import threading
from utilities.id_classification import classify
import sys
from restrict.urls import Urls
from restrict.sf_credentials import SfCredentials
from tkinter import END


def monitor_final(log_box_entry):
    sys.setrecursionlimit(300000)
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty(name='voice', value='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    def monitor():
        engine.say("monitoring...")
        engine.runAndWait()
        log_box_entry.insert(END, f'Monitoring... {datetime.now}')
        log_box_entry.insert(END, '\n')
        # print('Monitoring...', datetime.now())

        def login_to_sf():
            driver.get(Urls.lighting_to_classic_url)
            time.sleep(10)
            driver.get(Urls.salesforce_report_url)
            try:
                username = driver.find_element(By.ID, "username")
                username.send_keys(SfCredentials.username)
                password = driver.find_element(By.ID, "password")
                password.send_keys(SfCredentials.password)
                driver.find_element(By.ID, "Login").click()
                try:
                    driver.find_element(By.ID, "tryLexDialogX").click()
                except exceptions.NoSuchElementException:
                    driver.get(Urls.lighting_to_classic_url)
                    driver.get(Urls.salesforce_report_url)
                time.sleep(3)
                text = driver.find_element(By.ID, 'fchArea').text
                table = io.StringIO(text)
                df = pd.read_csv(table, sep=' ', header=None).iloc[1:-2, :-1]
                return df
            except exceptions.NoSuchElementException:
                text = driver.find_element(By.ID, 'fchArea').text
                table = io.StringIO(text)
                df = pd.read_csv(table, sep=' ', header=None).iloc[1:-2, :-1]
                return df

        def looping(df, counter):
            log_box_entry.insert(END, counter)
            log_box_entry.insert(END, '\n')
            while True:
                counter += 1
                driver.refresh()
                time.sleep(5)
                text1 = driver.find_element(By.ID, 'fchArea').text
                table1 = io.StringIO(text1)
                df1 = pd.read_csv(table1, sep=' ', header=None).iloc[1:-2, :-1]
                if df1.equals(df):
                    return looping(df1, counter)
                else:
                    frequency = 2500
                    duration = 300
                    winsound.Beep(frequency, duration)
                    engine.say("New account detected! Checking Documents...")
                    engine.runAndWait()
                    df2 = pd.concat([df1, df]).drop_duplicates(keep=False)
                    log_box_entry.insert(END, df2)
                    log_box_entry.insert(END, '\n')
                    accounts = df2.iloc[:, :1].values.tolist()
                    result = threading.Thread(target=classify(accounts)).start()
                    df = df1
                    return looping(df, counter)

        df_pre = login_to_sf()
        main_counter = 0
        looping(df_pre, main_counter)

    try:
        ser = Service("driver/chromedriver.exe")
        driver_options = webdriver.ChromeOptions()
        driver_options.add_experimental_option("detach", True)
        driver_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=ser, options=driver_options)
        driver.minimize_window()
        # monitor()
    except (exceptions.WebDriverException, exceptions.NoSuchElementException, AttributeError) as error:
        print(error)
        return monitor_final(log_box_entry)
