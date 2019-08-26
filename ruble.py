import requests
from bs4 import BeautifulSoup


def get_html():
    url = 'https://www.cbr.ru/currency_base/daily/'
    r = requests.get(url)
    return r.text

def get_rate(html):
    soup = BeautifulSoup(html, 'lxml')
    t = soup.find('td', text='USD').find_parent().find_all('td')[-1].text
    print(t)

def main():
    get_rate(get_html())


if __name__ == '__main__':
    main()
