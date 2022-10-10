import requests
from restrict.urls import Urls


def webhook_new_account(account):
    data = {
        "title": "New Account",
        "text": f"Account: {account}"
    }
    headers = {'Content-type': 'application/json'}
    res = requests.post(Urls.teams_webhook_url,
                        json=data, headers=headers)


def webhook_class_result(account, predictions, url_profile, idfront_src):
    if predictions:
        if 'Chinese ID FRONT' or 'Chinese ID BACK' in predictions:
            data = {
                "type": "message",
                "attachments": [
                    {
                        "contentType": "application/vnd.microsoft.card.hero",
                        "content": {
                            "title": f"Login ID: {account}",
                            "type": "Container",
                            "images": [
                                {
                                    "url": idfront_src
                                }
                            ],
                            "text": "ID documents have been detected, please process now!",
                            "subtitle": " ",
                            "buttons": [
                                {
                                    "type": "openUrl",
                                    "title": "BO Profile",
                                    "value": url_profile
                                },
                                {
                                    "type": "openUrl",
                                    "title": "View Documents",
                                    "value": url_profile + '?_tab=_11',
                                }
                            ]
                        }
                    }
                ]
            }
            header = {"Content-type": "application/json"}
            res = requests.post(Urls.teams_webhook_url,
                                json=data, headers=header)
        else:
            data = {
                "type": "message",
                "attachments": [
                    {
                        "contentType": "application/vnd.microsoft.card.hero",
                        "content": {
                            "title": f"Login ID: {account}",
                            "type": "Container",
                            "images": [
                                {
                                    "url": idfront_src
                                }
                            ],
                            "subtitle": " ",
                            "text": "Non-ID Images have been detected, please verify!",
                            "buttons": [
                                {
                                    "type": "openUrl",
                                    "title": "BO Profile",
                                    "value": url_profile
                                },
                                {
                                    "type": "openUrl",
                                    "title": "View Documents",
                                    "value": url_profile + '?_tab=_11',
                                }
                            ]
                        }
                    }
                ]
            }
            header = {"Content-type": "application/json"}
            res = requests.post(Urls.teams_webhook_url,
                                json=data, headers=header)
    else:
        data = {
                "type": "message",
                "attachments": [
                    {
                        "contentType": "application/vnd.microsoft.card.hero",
                        "content": {
                            "title": f"Login ID: {account}",
                            "type": "Container",
                            "images": [
                                {
                                    "url": 'https://statics.teams.cdn.office.net/evergreen-assets/apps/teams_dev_app_largeimage.png'
                                }
                            ],
                            "subtitle": " ",
                            "text": "No images have been detected, please check back!",
                            "buttons": [
                                {
                                    "type": "openUrl",
                                    "title": "BO Profile",
                                    "value": url_profile
                                },
                                {
                                    "type": "openUrl",
                                    "title": "View Documents",
                                    "value": url_profile + '?_tab=_11',
                                }
                            ]
                        }
                    }
                ]
            }
        header = {'Content-type': 'application/json'}
        res = requests.post(Urls.teams_webhook_url,
                            json=data, headers=header)


def webhook_not_found(account):
    data = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.hero",
                "content": {
                    "title": f"Login ID: {account}",
                    "type": "Container",
                    "images": [
                        {
                            "url": 'https://2.cdn.ekm.net/ekmps/shops/signmaker/images/prohibition-sign-no-access-8557--material-wv-white-self-adhesive-vinyl-47251-p.png?v=1462021-143501'
                        }
                    ],
                    "subtitle": " ",
                    "text": "No BO Access for this account!(Possible SCA)",
                }
            }
        ]
    }
    header = {'Content-type': 'application/json'}
    res = requests.post(Urls.teams_webhook_url,
                        json=data, headers=header)