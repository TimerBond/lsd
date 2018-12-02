import requests
import pandas as pd
import csv
from pprint import pprint


def main():
    logandpass()


def logandpass():  # Get login and password
    print('Login:')
    login = input()
    print('Password:')
    password = input()
    auth(login, password)


def auth(login, password):  # Authorization
    session = requests.Session()
    params = {
        'main_login': login,
        'main_password': password
    }
    session.post('https://edu.tatar.ru/logon',
                 headers={'Referer': 'https://edu.tatar.ru/start/logon-process'},
                 params=params)  # Authorization ends
    parsingterm(session.get('https://edu.tatar.ru/user/diary/term').text)


def parsingterm(html):
    df_list = pd.read_html(html)[0]
    df_list.to_csv('term.csv')
    parsingcsv()


def parsingcsv():
    d = {}
    with open('term.csv', encoding='utf-8', mode='r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        d = {}
        for el in reader:
            if len(el[0]) > 0:
                sub = el[1]
                marksofsub = []
                for ell in el[2:-4]:
                    marksofsub.append(ell)
                marksofsub = list(filter(lambda x: len(x) > 0 and x != 0.0, marksofsub))
                d[sub] = marksofsub
        subs = list(d.keys())[:-1]
        marks = list(d.values())
        sr = marks[-1][0]
        for i in range(len(subs)):
            print(subs[i], end=': ')
            if len(marks[i]) > 0:
                for k in range(len(marks[i])):
                    if k != len(marks[i]) - 1:
                        print(marks[i][k], end=', ')
                    else:
                        print(marks[i][k])
            else:
                print(0)
        print('Средний балл: ' + sr)


if __name__ == '__main__':
    main()
