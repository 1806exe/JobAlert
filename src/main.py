import requests
import time
from bs4 import BeautifulSoup as Soup


def kijiweni():
    print('Collecting data...')
    url = 'http://kijiwe.co.tz/'

    r = requests.get(url)
    html_contents = r.text

    html_soup = Soup(html_contents, 'html.parser')
    t = time.localtime()
    timestamp = time.strftime('%b-%d-%Y-%H%M', t)

    file_txt = open('../data/saved/kijiweni.txt ' + timestamp, 'w')
    tag = '******** ALL THIS DATA ARE COLLECTED FROM KIJIWENI.CO.TZ *************** \n'
    file_txt.write(tag)

    for found in html_soup.find_all('div', {'class': 'post'}):
        title = found.h2.text.upper()
        file_txt.write(title)
        file_txt.write('SOURCE LINK -> {}'.format(found.h2.a['href'] + '\n'))
        file_txt.write(('__' * 50))

    file_txt.close()
    print(' ')
    print('Finish to collect data from {}'.format(url))
    print('Data saved to ', file_txt.name)


if __name__ == '__main__':
    kijiweni()
