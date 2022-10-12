from tkinter import messagebox
from google_trans_new import google_translator
from utilities.Translator import Tesseract_Translator
from utilities.ninja_utilities import Utilities
import os
import tkinter
from tkinter import ttk
from fillpdf import fillpdfs
from bs4 import BeautifulSoup
import time
import urllib
from restrict.urls import Urls
from restrict.sf_credentials import SfCredentials
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import json
import threading

task_counter = 0


class NinjaFunctions:
    def __init__(self, email, client_id, first_name, last_name, login_session, status_label, variable):
        self._first_name = first_name.replace('\n', '')
        self._last_name = last_name.replace('\n', '')
        self._client_id = client_id.replace('\n', '')
        self._email = email.replace('/n', '')
        self._variable = variable
        self._session = login_session
        self._status_label = status_label
        self._Url = Urls()
        self._Uti = Utilities()
        self._ser = Service('driver/chromedriver.exe')
        self._normal_driver_option = webdriver.ChromeOptions()
        self._normal_driver_option.add_experimental_option('detach', True)
        self._normal_driver_option.add_experimental_option('excludeSwitches', ['enable-logging'])

    def _bs4(self, url):
        _r = self._session.get(url)
        _soup = BeautifulSoup(_r.content, 'html5lib')
        return _soup

    def _scrap(self):
        _url = f'{self._Url.profile_url}{self._client_id}/edit'
        _soup = self._bs4(_url)
        _token = _soup.find('input', attrs={'name': 's2276c242cd[_token]'})['value']
        tab = _soup.find('input', attrs={'name': '_tab'})
        real_type = _soup.find('select', attrs={'name': 's2276c242cd[real_type]'}).find('option', attrs={'selected': 'selected'})['value']
        company = _soup.find('select', attrs={'name': 's2276c242cd[company]'}).find('option', attrs={'selected': 'selected'})['value']
        try:
            bonusPercentage = _soup.find('input', attrs={'name': 's2276c242cd[bonusPercentage]'})['value']
        except KeyError:
            bonusPercentage = ''
        try:
            verificationPhone = _soup.find('select', attrs={'name': 's2276c242cd[verificationPhone]'}).find('option', attrs={'selected': 'selected'})['value']
        except AttributeError:
            verificationPhone = ''
        try:
            portalUserPlatform = _soup.find('select', attrs={'name': 's2276c242cd[PortalUser][Platform]'}).find('option', attrs={'selected': 'selected'})['value']
        except AttributeError:
            portalUserPlatform = ''
        portalUserAccountType = _soup.find('select', attrs={'name': 's2276c242cd[PortalUser][account_type]'}).find('option', attrs={'selected': 'selected'})['value']
        PortalUserUsername = _soup.find('input', attrs={'name': 's2276c242cd[PortalUser][username]'})['value']
        try:
            PortalUserAlternativeEmail = _soup.find('input', attrs={'name': 's2276c242cd[PortalUser][alternative_email]'})['value']
        except KeyError:
            PortalUserAlternativeEmail = ''
        try:
            PortalUserReferer = _soup.find('input', attrs={'name': 's2276c242cd[PortalUser][referer]'})['value']
        except KeyError:
            PortalUserReferer = ''
        try:
            PortalUserSalias = _soup.find('input', attrs={'name': 's2276c242cd[PortalUser][salias]'})['value']
        except KeyError:
            PortalUserSalias = ''

        PortalUserFirst_name = self._first_name
        PortalUserLast_name = self._last_name
        try:
            PortalUserDateOfBirthMonth = _soup.find('select', attrs={'name': 's2276c242cd[PortalUser][dateOfBirth][month]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            PortalUserDateOfBirthMonth = ''
        try:
            PortalUserDateOfBirthday = _soup.find('select', attrs={'name': 's2276c242cd[PortalUser][dateOfBirth][day]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            PortalUserDateOfBirthday = ''
        try:
            PortalUserDateOfBirthYear = _soup.find('select', attrs={'name': 's2276c242cd[PortalUser][dateOfBirth][year]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            PortalUserDateOfBirthYear = ''
        PortalUserCountry = _soup.find('select', attrs={'name': 's2276c242cd[PortalUser][country]'}).find('option', attrs={'selected': 'selected'})['value']
        try:
            PortalUserMobile = _soup.find('input', attrs={'name': 's2276c242cd[PortalUser][mobile_number]'})['value']
        except KeyError:
            PortalUserMobile = ''
        PortalUserCommunicationLanguage = _soup.find('select', attrs={'name': 's2276c242cd[PortalUser][communicationLanguage]'}).find('option', attrs={'selected': 'selected'})['value']
        try:
            title = _soup.find('select', attrs={'name': 's2276c242cd[title]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            title = ''
        try:
            maritalStatus = _soup.find('select', attrs={'name': 's2276c242cd[maritalStatus]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            maritalStatus = ''
        try:
            isWholeSale = _soup.find('select', attrs={'name': 's2276c242cd[isWholeSale]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            isWholeSale = ''
        try:
            accountInformation_tradingCurrency = _soup.find('select', attrs={'name': 's2276c242cd[isWholeSale]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            accountInformation_tradingCurrency = ''
        try:
            accountInformation_expectedFirstDeposit = _soup.find('input', attrs={'name': 's2276c242cd[accountInformation__expectedFirstDeposit]'})['value']
        except KeyError:
            accountInformation_expectedFirstDeposit = ''
        try:
            accountInformation_leverage = _soup.find('select', attrs={'name': 's2276c242cd[accountInformation__leverage]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            accountInformation_leverage = ''
        try:
            accountInformation_lotSize = _soup.find('select', attrs={'name': 's2276c242cd[accountInformation__lotSize]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            accountInformation_lotSize = ''
        try:
            canTransferAccount = _soup.find('select', attrs={'name': 's2276c242cd[canTransferAccount]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            canTransferAccount = ''
        try:
            accountInformation_orderType = _soup.find('select', attrs={'name': 's2276c242cd[accountInformation__orderType]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            accountInformation_orderType = ''
        try:
            financeTradingInformation__haveCriminalRecord = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__haveCriminalRecord]'}).find('option', attrs={'selected': 'selected'})['value']
        except (TypeError, AttributeError):
            financeTradingInformation__haveCriminalRecord = ''
        try:
            primaryContactNumber = _soup.find('input', attrs={'name': 's2276c242cd[primaryContactNumber]'})['value']
        except KeyError:
            primaryContactNumber = ''
        try:
            workPhoneNumber = _soup.find('input', attrs={'name': 's2276c242cd[workPhoneNumber]'})['value']
        except (KeyError, TypeError):
            workPhoneNumber = ''
        try:
            mobilePhoneNumber = _soup.find('input', attrs={'name': 's2276c242cd[mobilePhoneNumber]'})['value']
        except KeyError:
            mobilePhoneNumber = ''
        try:
            address_streetName = _soup.find('input', attrs={'name': 's2276c242cd[address__streetName]'})['value']
        except KeyError:
            address_streetName = ''
        try:
            address_buildingNameNumber = _soup.find('input', attrs={'name': 's2276c242cd[address__buildingNameNumber]'})['value']
        except KeyError:
            address_buildingNameNumber = ''
        try:
            address_stateProvince = _soup.find('input', attrs={'name': 's2276c242cd[address__stateProvince]'})['value']
        except KeyError:
            address_stateProvince = ''
        try:
            address_cityTown = _soup.find('input', attrs={'name': 's2276c242cd[address__cityTown]'})['value']
        except KeyError:
            address_cityTown = ''
        try:
            webSourceInformation_ipCountry = _soup.find('input', attrs={'name': 's2276c242cd[webSourceInformation__ipCountry]'})['value']
        except KeyError:
            webSourceInformation_ipCountry = ''
        try:
            address_postalCode = _soup.find('input', attrs={'name': 's2276c242cd[address__postalCode]'})['value']
        except KeyError:
            address_postalCode = ''
        try:
            idType = _soup.find('select', attrs={'name': 's2276c242cd[idType]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            idType = ''
        try:
            personal_id = _soup.find('input', attrs={'name': 's2276c242cd[personal_id]'})['value']
        except KeyError:
            personal_id = ''
        try:
            altEmail = _soup.find('input', attrs={'name': 's2276c242cd[altEmail]'})['value']
        except KeyError:
            altEmail = ''
        try:
            employmentInformation_employmentStatus = _soup.find('select', attrs={'name': 's2276c242cd[employmentInformation__employmentStatus]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            employmentInformation_employmentStatus = ''
        try:
            employmentInformation_sourceOfFunds = _soup.find('input', attrs={'name': 's2276c242cd[employmentInformation__sourceOfFunds]'})['value']
        except KeyError:
            employmentInformation_sourceOfFunds = ''
        try:
            employmentInformation_businessSector = _soup.find('input', attrs={'name': 's2276c242cd[employmentInformation__businessSector]'})['value']
        except KeyError:
            employmentInformation_businessSector = ''
        try:
            employmentInformation_corporateName = _soup.find('input', attrs={'name': 's2276c242cd[employmentInformation__corporateName]'})['value']
        except KeyError:
            employmentInformation_corporateName = ''
        try:
            employmentInformation_employmentYears = _soup.find('select', attrs={'name': 's2276c242cd[employmentInformation__employmentYears]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            employmentInformation_employmentYears = ''
        try:
            employmentInformation_occupation = _soup.find('input', attrs={'name': 's2276c242cd[employmentInformation__occupation]'})['value']
        except KeyError:
            employmentInformation_occupation = ''
        try:
            financeTradingInformation_riskProfile = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__riskProfile]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation_riskProfile = ''
        try:
            financeTradingInformation_tradingObjectives = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__tradingObjectives]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation_tradingObjectives = ''
        try:
            financeTradingInformation_annualIncome = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__annualIncome]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation_annualIncome = ''
        try:
            financeTradingInformation_netWorth = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__annualIncome]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation_netWorth = ''
        try:
            financeTradingInformation_riskCapital = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__riskCapital]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation_riskCapital = ''
        try:
            financeTradingInformation_nameOfAttorney = _soup.find('input', attrs={'name': 's2276c242cd[financeTradingInformation__nameOfAttorney]'})['value']
        except KeyError:
            financeTradingInformation_nameOfAttorney = ''
        try:
            financeTradingInformation__attorneyLocation = _soup.find('input', attrs={'name': 's2276c242cd[financeTradingInformation__attorneyLocation]'})['value']
        except KeyError:
            financeTradingInformation__attorneyLocation = ''
        try:
            financeTradingInformation_attorneyIncentiveFees = _soup.find('input', attrs={'name': 's2276c242cd[financeTradingInformation__attorneyIncentiveFees]'})['value']
        except KeyError:
            financeTradingInformation_attorneyIncentiveFees = ''
        try:
            financeTradingInformation__attorneyOtherFees = _soup.find('input', attrs={'name': 's2276c242cd[financeTradingInformation__attorneyOtherFees]'})['value']
        except KeyError:
            financeTradingInformation__attorneyOtherFees = ''
        try:
            financeTradingInformation__attorneyManagmentFees = _soup.find('input', attrs={'name': 's2276c242cd[financeTradingInformation__attorneyManagmentFees]'})['value']
        except KeyError:
            financeTradingInformation__attorneyManagmentFees = ''
        try:
            financeTradingInformation__attorneyIncentivePerDuration = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__attorneyIncentivePerDuration]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation__attorneyIncentivePerDuration = ''
        try:
            financeTradingInformation__accountTradedByAnother = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__accountTradedByAnother]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation__accountTradedByAnother = ''
        try:
            financeTradingInformation__attorneyManagmentPerDuration = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__attorneyManagmentPerDuration]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation__attorneyManagmentPerDuration = ''
        try:
            financeTradingInformation__attorneyOtherPerDuration = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__attorneyOtherPerDuration]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation__attorneyOtherPerDuration = ''
        try:
            financeTradingInformation__haveOtherFinancialInterest = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__haveOtherFinancialInterest]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation__haveOtherFinancialInterest = ''
        try:
            financeTradingInformation__useScalpingStrategies = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__useScalpingStrategies]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation__useScalpingStrategies = ''
        try:
            financeTradingInformation__useExpertAdvisor = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__useExpertAdvisor]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation__useExpertAdvisor = ''
        try:
            financeTradingInformation__useTradingCfd = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__useTradingCfd]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation__useTradingCfd = ''
        try:
            financeTradingInformation__inPendingBankruptcy = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__inPendingBankruptcy]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation__inPendingBankruptcy = ''
        try:
            financeTradingInformation__acceptElectronicTrading = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__acceptElectronicTrading]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation__acceptElectronicTrading = ''
        try:
            financeTradingInformation__haveLeverageExperience = _soup.find('select', attrs={'name': 's2276c242cd[financeTradingInformation__haveLeverageExperience]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            financeTradingInformation__haveLeverageExperience = ''
        try:
            tradingExperience__experienceStockSecurities = _soup.find('select', attrs={'name': 's2276c242cd[tradingExperience__experienceStockSecurities]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            tradingExperience__experienceStockSecurities = ''
        try:
            tradingExperience__experienceOptions = _soup.find('select', attrs={'name': 's2276c242cd[tradingExperience__experienceOptions]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            tradingExperience__experienceOptions = ''
        try:
            tradingExperience__experienceCommodities = _soup.find('select', attrs={'name': 's2276c242cd[tradingExperience__experienceCommodities]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            tradingExperience__experienceCommodities = ''
        try:
            tradingExperience__experienceForex = _soup.find('select', attrs={'name': 's2276c242cd[tradingExperience__experienceForex]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            tradingExperience__experienceForex = ''
        try:
            tradingExperience__experienceFutures = _soup.find('select', attrs={'name': 's2276c242cd[tradingExperience__experienceFutures]'}).find('option', attrs={'selected': 'selected'})['value']
        except TypeError:
            tradingExperience__experienceFutures = ''
        try:
            ibInformation__defaultSpread = _soup.find('input', attrs={'name': 's2276c242cd[ibInformation__defaultSpread]'})['value']
        except KeyError:
            ibInformation__defaultSpread = ''
        try:
            ibInformation__ibAddedSpread = _soup.find('input', attrs={'name': 's2276c242cd[ibInformation__ibAddedSpread]'})['value']
        except KeyError:
            ibInformation__ibAddedSpread = ''
        try:
            ibInformation__ibCommission = _soup.find('input', attrs={'name': 's2276c242cd[ibInformation__ibCommission]'})['value']
        except KeyError:
            ibInformation__ibCommission = ''
        try:
            ibInformation__originalRebate = _soup.find('input', attrs={'name': 's2276c242cd[ibInformation__originalRebate]'})['value']
        except KeyError:
            ibInformation__originalRebate = ''
        try:
            ibInformation__specialOffer = _soup.find('input', attrs={'s2276c242cd[ibInformation__specialOffer]'})['value']
        except (KeyError, TypeError):
            ibInformation__specialOffer = ''
        try:
            ibInformation__specialOffer2 = _soup.find('input', attrs={'s2276c242cd[ibInformation__specialOffer2]'})['value']
        except (KeyError, TypeError):
            ibInformation__specialOffer2 = ''

        form = {
            'uniqid': 's2276c242cd',
            's2276c242cd[real_type]': real_type,
            's2276c242cd[company]': company,
            's2276c242cd[bonusPercentage]': bonusPercentage,
            's2276c242cd[verificationPhone]': verificationPhone,
            's2276c242cd[PortalUser][Platform]': portalUserPlatform,
            's2276c242cd[PortalUser][account_type]': portalUserAccountType,
            's2276c242cd[PortalUser][username]': PortalUserUsername,
            's2276c242cd[PortalUser][alternative_email]': PortalUserAlternativeEmail,
            's2276c242cd[PortalUser][referer]': PortalUserReferer,
            's2276c242cd[PortalUser][salias]': PortalUserSalias,
            's2276c242cd[PortalUser][first_name]': PortalUserFirst_name,
            's2276c242cd[PortalUser][last_name]': PortalUserLast_name,
            's2276c242cd[PortalUser][dateOfBirth][month]': PortalUserDateOfBirthMonth,
            's2276c242cd[PortalUser][dateOfBirth][day]': PortalUserDateOfBirthday,
            's2276c242cd[PortalUser][dateOfBirth][year]': PortalUserDateOfBirthYear,
            's2276c242cd[PortalUser][country]': PortalUserCountry,
            's2276c242cd[PortalUser][mobile_number]': PortalUserMobile,
            's2276c242cd[PortalUser][communicationLanguage]': PortalUserCommunicationLanguage,
            's2276c242cd[title]': title,
            's2276c242cd[maritalStatus]': maritalStatus,
            's2276c242cd[isWholeSale]': isWholeSale,
            's2276c242cd[accountInformation__tradingCurrency]': accountInformation_tradingCurrency,
            's2276c242cd[accountInformation__expectedFirstDeposit]': accountInformation_expectedFirstDeposit,
            's2276c242cd[accountInformation__leverage]': accountInformation_leverage,
            's2276c242cd[accountInformation__lotSize]': accountInformation_lotSize,
            's2276c242cd[canTransferAccount]': canTransferAccount,
            's2276c242cd[accountInformation__orderType]': accountInformation_orderType,
            's2276c242cd[financeTradingInformation__haveCriminalRecord]': financeTradingInformation__haveCriminalRecord,
            's2276c242cd[primaryContactNumber]': primaryContactNumber,
            's2276c242cd[workPhoneNumber]': workPhoneNumber,
            's2276c242cd[mobilePhoneNumber]': mobilePhoneNumber,
            's2276c242cd[address__streetName]': address_streetName,
            's2276c242cd[address__buildingNameNumber]': address_buildingNameNumber,
            's2276c242cd[address__stateProvince]': address_stateProvince,
            's2276c242cd[address__cityTown]': address_cityTown,
            's2276c242cd[webSourceInformation__ipCountry]': webSourceInformation_ipCountry,
            's2276c242cd[address__postalCode]': address_postalCode,
            's2276c242cd[idType]': idType,
            's2276c242cd[personal_id]': personal_id,
            's2276c242cd[altEmail]': altEmail,
            's2276c242cd[employmentInformation__employmentStatus]': employmentInformation_employmentStatus,
            's2276c242cd[employmentInformation__sourceOfFunds]': employmentInformation_sourceOfFunds,
            's2276c242cd[employmentInformation__businessSector]': employmentInformation_businessSector,
            's2276c242cd[employmentInformation__corporateName]': employmentInformation_corporateName,
            's2276c242cd[employmentInformation__employmentYears]': employmentInformation_employmentYears,
            's2276c242cd[employmentInformation__occupation]': employmentInformation_occupation,
            's2276c242cd[financeTradingInformation__riskProfile]': financeTradingInformation_riskProfile,
            's2276c242cd[financeTradingInformation__tradingObjectives]': financeTradingInformation_tradingObjectives,
            's2276c242cd[financeTradingInformation__annualIncome]': financeTradingInformation_annualIncome,
            's2276c242cd[financeTradingInformation__netWorth]': financeTradingInformation_netWorth,
            's2276c242cd[financeTradingInformation__riskCapital]': financeTradingInformation_riskCapital,
            's2276c242cd[financeTradingInformation__nameOfAttorney]': financeTradingInformation_nameOfAttorney,
            's2276c242cd[financeTradingInformation__attorneyLocation]': financeTradingInformation__attorneyLocation,
            's2276c242cd[financeTradingInformation__attorneyIncentiveFees]': financeTradingInformation_attorneyIncentiveFees,
            's2276c242cd[financeTradingInformation__attorneyOtherFees]': financeTradingInformation__attorneyOtherFees,
            's2276c242cd[financeTradingInformation__attorneyManagmentFees]': financeTradingInformation__attorneyManagmentFees,
            's2276c242cd[financeTradingInformation__attorneyIncentivePerDuration]': financeTradingInformation__attorneyIncentivePerDuration,
            's2276c242cd[financeTradingInformation__accountTradedByAnother]': financeTradingInformation__accountTradedByAnother,
            's2276c242cd[financeTradingInformation__attorneyManagmentPerDuration]': financeTradingInformation__attorneyManagmentPerDuration,
            's2276c242cd[financeTradingInformation__attorneyOtherPerDuration]': financeTradingInformation__attorneyOtherPerDuration,
            's2276c242cd[financeTradingInformation__haveOtherFinancialInterest]': financeTradingInformation__haveOtherFinancialInterest,
            's2276c242cd[financeTradingInformation__useScalpingStrategies]': financeTradingInformation__useScalpingStrategies,
            's2276c242cd[financeTradingInformation__useExpertAdvisor]': financeTradingInformation__useExpertAdvisor,
            's2276c242cd[financeTradingInformation__useTradingCfd]': financeTradingInformation__useTradingCfd,
            's2276c242cd[financeTradingInformation__inPendingBankruptcy]': financeTradingInformation__inPendingBankruptcy,
            's2276c242cd[financeTradingInformation__acceptElectronicTrading]': financeTradingInformation__acceptElectronicTrading,
            's2276c242cd[financeTradingInformation__haveLeverageExperience]': financeTradingInformation__haveLeverageExperience,
            's2276c242cd[tradingExperience__experienceStockSecurities]': tradingExperience__experienceStockSecurities,
            's2276c242cd[tradingExperience__experienceOptions]': tradingExperience__experienceOptions,
            's2276c242cd[tradingExperience__experienceCommodities]': tradingExperience__experienceCommodities,
            's2276c242cd[tradingExperience__experienceForex]': tradingExperience__experienceForex,
            's2276c242cd[tradingExperience__experienceFutures]': tradingExperience__experienceFutures,
            's2276c242cd[ibInformation__defaultSpread]': ibInformation__defaultSpread,
            's2276c242cd[ibInformation__ibAddedSpread]': ibInformation__ibAddedSpread,
            's2276c242cd[ibInformation__ibCommission]': ibInformation__ibCommission,
            's2276c242cd[ibInformation__originalRebate]': ibInformation__originalRebate,
            's2276c242cd[ibInformation__specialOffer]': ibInformation__specialOffer,
            's2276c242cd[ibInformation__specialOffer2]': ibInformation__specialOffer2,
            '_tab': tab,
            's2276c242cd[_token]': _token,
            'btn_update_and_edit': '',
        }
        return form

    def _change_form(self):
        self._status_label.config(text='Updating client info...\n')
        _form = self._scrap()
        _change_form = self._session.post(f'{self._Url.profile_url}{self._client_id}/edit', data=_form)
        self._status_label.config(text="Client's name updated...\n")
        return _change_form.ok

    def _before_uploading(self):
        _url = f'{self._Url.profile_url}{self._client_id}/show'
        _soup = self._bs4(_url)
        _src = _soup.find_all('img', attrs={'class': 'img-fluid width2'})
        _idfront_src = _soup.find('img', attrs={'class': 'img-fluid width2'}).get('src')
        _new_login_session = self._Uti.login()
        _generate_pdf = _new_login_session.get(f'{self._Url.gen_pdf_url}{self._client_id}')
        _r = _new_login_session.get(_url)
        _soup = BeautifulSoup(_r.content, 'html5lib')
        _pdf = _soup.find('span', attrs={'class': 'gen_pdf'}).find('a')['href']
        self._status_label.config(text='All files download completed...\n')

        return _idfront_src, _pdf

    def _approve(self):
        _approve_id = self._session.get(f'{self._Url.bo_approve_id}{self._client_id}')
        self._status_label.config(text='ID is approved...\n')
        _approve_por = self._session.get(f'{self._Url.bo_approve_por}{self._client_id}')
        self._status_label.config(text='POR is approved...\n')

    def _upload_files(self):
        _cotFile = None
        _cotFile_name = None
        try:
            _cotFile = open(f'{self._Url.os_path}{self._first_name}{self._last_name}_COT.pdf', 'rb')
            _cotFile_name = f'{self._first_name}{self._last_name}_COT.pdf'
        except FileNotFoundError:
            tkinter.messagebox.showerror(title='Warning', message='No COT find!')
            exit()
        _documents = self._before_uploading()
        _id_front = _documents[0]
        _appFile = _documents[1]
        urllib.request.urlretrieve(_appFile, f'{self._Url.os_path}{self._email}\\{self._first_name}{self._last_name}_APP.pdf')
        self._status_label.config(text='Uploading all files...\n')

        _filetype = ['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG']
        _id_file = ""
        _id_file_name = ""

        for _f in _filetype:
            if _f in _id_front:
                _id_file = f'{self._Url.os_path}{self._email}\\{self._first_name}{self._last_name}_idfront.{_f}'
                _id_file_name = f'{self._first_name}{self._last_name}_idfront.{_f}'
                urllib.request.urlretrieve(_id_front, _id_file)

        _appFile = f'{self._Url.os_path}{self._email}\\{self._first_name}{self._last_name}_APP.pdf'
        _appFile_name = f'{self._first_name}{self._last_name}_APP.pdf'
        _appFile = open(_appFile, 'rb')
        _id_file = open(_id_file, 'rb')

        _por_data = {
            'type': (None, 'POR1-upload'),
            'file': (_id_file_name, _id_file, 'image/jpeg')
        }

        _cot_data = {
            'type': (None, 'POR2-upload'),
            'file': (_cotFile_name, _cotFile, 'application/pdf')
        }

        _app_data = {
            'type': (None, 'LPOA1-upload'),
            'file': (_appFile_name, _appFile, 'application/pdf')
        }

        _por1_url = f'{self._Url.bo_upload_file}{self._client_id}?type=POR1-upload'
        _por2_url = f'{self._Url.bo_upload_file}{self._client_id}?type=POR2-upload'
        _LPOA1_url = f'{self._Url.bo_upload_file}{self._client_id}?type=LPOA1-upload'

        self._session.post(_por1_url, files=_por_data)
        self._session.post(_por2_url, files=_cot_data)
        self._session.post(_LPOA1_url, files=_app_data)
        self._status_label.config(text='Files uploaded successfully...\n')

        self._approve()

    def _upload_file_other(self):
        _documents = self._before_uploading()
        _appFile = _documents[1]
        urllib.request.urlretrieve(_appFile, f'{self._Url.os_path}{self._email}\\{self._first_name}{self._last_name}_APP.pdf')
        _appFile = f'{self._Url.os_path}{self._email}\\{self._first_name}{self._last_name}_APP.pdf'
        _appFile_name = f'{self._first_name}{self._last_name}_APP.pdf'
        _appFile = open(_appFile, 'rb')

        _app_data = {
            'type': (None, 'POR2-upload'),
            'file': (_appFile_name, _appFile, 'application/pdf')
        }

        _por2_url = f'{self._Url.bo_upload_file}{self._client_id}?type=POR2-upload'
        _uploading_app = self._session.post(_por2_url, files=_app_data)
        self._status_label.config(text='Files uploaded successfully...\n')
        self._approve()

    def _open_salesforce_other(self):
        _salesforce_driver = webdriver.Chrome(service=self._ser, options=self._normal_driver_option)
        _salesforce_driver.get(self._Url.salesforce_login_url)
        _username = _salesforce_driver.find_element(By.NAME, 'username')
        _username.send_keys(SfCredentials.username)
        _password = _salesforce_driver.find_element(By.NAME, 'pw')
        _password.send_keys(SfCredentials.password)
        _salesforce_driver.find_element(By.NAME, 'Login').click()
        _salesforce_driver.find_element(By.XPATH, '//*[@id="tryLexDialogX"]').click()
        _salesforce_driver.find_element(By.ID, 'phSearchInput').send_keys(self._email)
        _salesforce_driver.find_element(By.ID, 'phSearchButton').click()
        Wait(_salesforce_driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="Account_body"]/table/tbody/tr[2]/th/a'))).click()
        time.sleep(2)
        _trading_accounts = _salesforce_driver.find_elements(By.XPATH, '//*[contains(@class,"bPageBlock brandSecondaryBrd secondaryPalette")]')[1]
        try:
            _trading_account = _trading_accounts.find_elements(By.XPATH, '//a[contains(@title, "33")]')[-1].click()
        except IndexError:
            _trading_account = _trading_accounts.find_elements(By.XPATH, '//a[contains(@title, "88")]')[-1].click()

        self._status_label.config(text='Please update the description...\n')

    def _open_salesforce(self):
        _salesforce_driver = webdriver.Chrome(service=self._ser, options=self._normal_driver_option)
        _salesforce_driver.get(self._Url.salesforce_login_url)
        _username = _salesforce_driver.find_element(By.NAME, 'username')
        _username.send_keys(SfCredentials.username)
        _password = _salesforce_driver.find_element(By.NAME, 'pw')
        _password.send_keys(SfCredentials.password)
        _salesforce_driver.find_element(By.NAME, 'Login').click()
        _salesforce_driver.find_element(By.XPATH, '//*[@id="tryLexDialogX"]').click()
        _salesforce_driver.find_element(By.ID, 'phSearchInput').send_keys(self._email)
        _salesforce_driver.find_element(By.ID, 'phSearchButton').click()
        time.sleep(4)
        _salesforce_driver.find_element(By.XPATH, '//*[@id='"Contact_body"']/table/tbody/tr[2]/td[1]/a').click()
        time.sleep(2)
        _salesforce_driver.find_element(By.ID, '00N0I00000JsRdF').clear()
        self._status_label.config(text='Please update the local name...\n')

    def _bo_all(self):
        self._variable.set('Type')
        self._change_form()
        self._upload_files()
        self._open_salesforce()

    def _bo_all_other(self):
        self._variable.set('Type')
        self._change_form()
        self._upload_file_other()
        self._open_salesforce_other()

    def idDocuments(self):
        try:
            os.makedirs(self._Url.os_path + self._email)
            self._status_label.config(text="Creating client's folder...\n")
        except OSError:
            tkinter.messagebox.showerror(title='Warning', message='The folder is already exist!')
        self._status_label.config(text='Start downloading...\n')
        _url = self._Url.profile_url + self._client_id + '/show'
        _soup = self._bs4(_url)
        _src = _soup.find_all('img', attrs={'class': 'img-fluid width2'})
        _file_format = ['jpg', 'pdf', 'jpeg', 'png', 'JPG']
        try:
            _idfront_src = _soup.find('img', attrs={'class': 'img-fluid width2'}).get('src')
            for _source in _src:
                for _f in _file_format:
                    if _f in _source.get('src'):
                        _file_name = f'{self._Url.os_path_f}/{self._email}/{self._first_name}{self._last_name}{int(time.time())}.{_f}'
                        urllib.request.urlretrieve(_source.get('src'), _file_name)
                        os.startfile(_file_name)
            _new_login_session = self._Uti.login()
            _generate_pdf = _new_login_session.get(self._Url.pdfUrl(self._client_id))
            _soup = self._bs4(_url)
            _pdf = _soup.find('span', attrs={'class': 'gen_pdf'}).find('a')['href']
            self._status_label.config(text='All files download completed...\n')
            return _idfront_src, _pdf
        except AttributeError:
            self._status_label.config(text='No files uploaded...\n')

    def idTranslation(self):
        _Translator = google_translator()
        _Data_Generator = Tesseract_Translator()
        try:
            os.makedirs(self._Url.os_path + self._email)
        except OSError:
            tkinter.messagebox.showerror(title='Warning', message='The folder is already exist!')

        _format_path = 'cot/COT_Format.pdf'
        _output_path = self._Url.os_path + self._email + '\\' + self._first_name + self._last_name + '_COT.pdf'
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
        _driver = webdriver.Chrome(service=self._ser, options=self._normal_driver_option)
        _driver.maximize_window()
        _bo_url = Urls.profile_url + self._client_id + '/show'
        _driver.get(_bo_url)
        with open('restrict/bo_credentials.json', 'r') as fp:
            _login_data = json.load(fp)
        _username = _driver.find_element(By.NAME, 'admin_username')
        _username.send_keys(_login_data['admin_username'])
        _password = _driver.find_element(By.NAME, 'admin_password')
        _password.send_keys(_login_data['admin_password'])
        _driver.find_element(By.CLASS_NAME, 'col-xs-4').click()

    def radiobuttonOption(self):
        _choice = self._variable.get()
        if _choice == "China":
            self._bo_all()
        elif _choice == "Other":
            self._bo_all_other()
        else:
            tkinter.messagebox.showerror(title='Warning', message='Please select the country!')


def delete_task(empty_order_label, client_id_label, email_entry,first_name_label, action_trans_id_button, last_name_label, action_run_button, action_show_id_button, action_vist_bo_button, action_del_button, status_label):
    empty_order_label.place_forget()
    client_id_label.place_forget()
    email_entry.place_forget()
    action_trans_id_button.place_forget()
    first_name_label.place_forget()
    last_name_label.place_forget()
    action_run_button.place_forget()
    action_show_id_button.place_forget()
    action_vist_bo_button.place_forget()
    action_del_button.place_forget()
    status_label.place_forget()


def add_task(variable, trans_btn, del_btn, run_btn, id_btn, eye_btn, email_entry, client_id_entry, first_name_entry, last_name_entry, root, login_session):
    global task_counter
    new_task_counter = task_counter + 1
    for cou in range(task_counter, new_task_counter):
        empty_order_label = ttk.Label(root, text=str(cou + 1), style='White_small.TLabel')
        empty_order_label.place(x=25, y=250 + 25 * (cou - 1))

        email_label = ttk.Label(root, text=email_entry.get(), style='White_small.TLabel')
        email_label.place(x=65, y=250 + 25 * (cou - 1))
        email = email_label.cget('text')

        client_id_label = ttk.Label(root, text=client_id_entry.get(), style='White_small.TLabel')
        client_id_label.place(x=277, y=250 + 25 * (cou - 1))
        client_id = client_id_label.cget('text')

        first_name_label = ttk.Label(root, text=first_name_entry.get(), style='White_small.TLabel')
        first_name_label.place(x=371, y=250 + 25 * (cou - 1))
        first_name = first_name_label.cget('text')

        last_name_label = ttk.Label(root, text=last_name_entry.get(), style='White_small.TLabel')
        last_name_label.place(x=518, y=250 + 25 * (cou - 1))
        last_name = last_name_label.cget('text')

        status_label = ttk.Label(root, text='', style='White_small.TLabel')
        status_label.place(x=663, y=250 + 25 * (cou - 1))

        NinjaFunction = NinjaFunctions(email, client_id, first_name, last_name, login_session, status_label, variable)

        action_run_button = tkinter.Button(root, bg='#202023', fg='white', image=run_btn, border=0, activebackground='#202023', activeforeground='white',
                                           command=lambda: threading.Thread(target=NinjaFunction.radiobuttonOption).start())
        action_visit_button = tkinter.Button(root, bg='#202023', fg='white', image=eye_btn, border=0, activebackground='#202023', activeforeground='white',
                                             command=lambda: threading.Thread(target=NinjaFunction.bo_check).start())
        action_show_id_button = tkinter.Button(root, bg='#202023', fg='white', image=id_btn, border=0, activebackground='#202023', activeforeground='white',
                                               command=lambda: threading.Thread(target=NinjaFunction.idDocuments).start())
        action_trans_id_button = tkinter.Button(root, bg='#202023', fg='white', image=trans_btn, border=0, activebackground='#202023', activeforeground='white',
                                                command=lambda: threading.Thread(target=NinjaFunction.idTranslation).start())
        action_del_button = tkinter.Button(root, bg='#202023', fg='white', image=del_btn, border=0, activebackground='#202023', activeforeground='white',
                                           command=lambda: threading.Thread(target=delete_task, args=(empty_order_label, client_id_label, email_label, first_name_label, action_trans_id_button, last_name_label, action_run_button, action_show_id_button, action_visit_button, action_del_button, status_label)).start())

        action_run_button.place(x=870, y=250 + 25 * (cou - 1))
        action_visit_button.place(x=957, y=249 + 25 * (cou - 1))
        action_show_id_button.place(x=895, y=249 + 25 * (cou - 1))
        action_trans_id_button.place(x=930, y=249 + 25 * (cou - 1))
        action_del_button.place(x=990, y=249 + 25 * (cou - 1))
        task_counter = new_task_counter
