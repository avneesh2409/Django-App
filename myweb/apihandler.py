import requests


def apirequest(url = "https://vue-http-86b74.firebaseio.com/userData.json"):
    res = requests.get(url)
    return res.json()
                                