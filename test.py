import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd


def main():
    logandpass()


def logandpass():
    login = '4702014096'
    password = 'waFB3rT$'
    auth(login, password)


def auth(login, password):
    session = requests.Session()
    params = {
        'main_login': login,
        'main_password': password
    }
    session.post('https://edu.tatar.ru/logon',
                 headers={'Referer': 'https://edu.tatar.ru/start/logon-process'},
                 params=params)
    parsing(session.get('https://edu.tatar.ru/user/diary/term').text)


def parsing(html):
    df = pd.read_html(html, header=1)
    print(df)


if __name__ == '__main__':
    main()
