"""
    Author: 1806exe
    Email: 1806exe@gmail.com
    GitHub: https://www.github.com/1806exe
"""

import os
import time
import tldextract
import requests
from bs4 import BeautifulSoup as Soup

def create_dirs():
    t = time.localtime()
    timestamp = time.strftime('%b-%Y', t)
    path = r'..\data\saved\{}'.format(timestamp)
    if not os.path.exists(path):
        os.makedirs(path)


def setup(url):
    ext = tldextract.extract(url)
    print("Collecting data from {0} Website.......".format(ext.domain))

def kijiweni():
    print('Collecting data...')
    url = 'http://kijiwe.co.tz'
    r = requests.get(url)
    html_contents = r.text
    html_soup = Soup(html_contents, 'html.parser')
    _time = time.localtime()
    timestamp = time.strftime('%d-%m-%Y %H-%M', _time)
    dir_name = time.strftime('%b-%Y', _time)
    file_txt = open('../data/saved/{}/{}.txt '.format(dir_name, name) + timestamp, 'w')
    tag = '******** JOB AVAILABLE TODAY {} *************** \n'.format(timestamp)
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

def ajira_portal():
    url = "http://portal.ajira.go.tz/index.php/advert"
    request = requests.get(url)
    html_context = request.text
    clean_data = Soup(html_context, "html.parser")

    for data in clean_data.find_all("tr", {'class', 'even'}):
        print(data.h5.text)
        print('Source --> {}'.format(data.h5.a['href']))
        print("--" * 40)

if __name__ == '__main__':
    #create_dirs()
    #kijiweni()
    setup('http://kijiwe.co.tz')
