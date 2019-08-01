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


# for space between
def space_btn(n):
    for i in range(n):
        print(" ")


def create_dirs():
    t = time.localtime()
    datestamp = time.strftime('%b-%Y', t)
    timestamp = time.strftime('%H%M')
    path = r'..\data\saved\{}'.format(datestamp)
    if not os.path.exists(path):
        os.makedirs(path)


def extract_domain(url):
    ext = tldextract.extract(url)
    domain = ext.domain
    return domain


def setup(url):
    space_btn(3)
    print("Collecting data from {0} Website.......".format(extract_domain(url)))
    r = requests.get(url)
    html_contents = r.text
    html_soup = Soup(html_contents, 'html.parser')
    return html_soup


def kijiweni():
    # call setUp function
    url = 'http://kijiwe.co.tz'
    html = setup(url)
    _time = time.localtime()
    timestamp = time.strftime('%d-%m-%Y %H%M', _time)
    dir_name = time.strftime('%b-%Y', _time)
    file_txt = open('../data/saved/{}/{}.txt '.format(dir_name, extract_domain(url).upper()) + timestamp, 'w')
    tag = '******** JOB AVAILABLE TODAY {} *************** \n'.format(timestamp)
    file_txt.write(tag)
    for found in html.find_all('div', {'class': 'post'}):
        title = found.h2.text.upper()
        file_txt.write(title)
        file_txt.write('SOURCE LINK -> {}'.format(found.h2.a['href'] + '\n'))
        file_txt.write(('__' * 50))

    file_txt.close()
    print(' ')
    print('Finish to collect data from {}'.format(url))
    print('Data saved to ', file_txt.name)
    space_btn(2)


def ajira_portal():
    url = "http://portal.ajira.go.tz/index.php/advert"
    html = setup(url)
    _time = time.localtime()
    timestamp = time.strftime('%d-%m-%Y %H%M', _time)
    dir_name = time.strftime('%b-%Y', _time)
    file_txt = open('../data/saved/{}/{}.txt '.format(dir_name, extract_domain(url).upper()) + timestamp, 'w')
    tag = '******** JOB AVAILABLE TODAY {} *************** \n'.format(timestamp)
    file_txt.write(tag)
    for data in html.find_all("tr", {'class', 'even'}):
        title = data.h5.text
        file_txt.write(title)
        file_txt.write('Source --> {}'.format(data.h5.a['href']))
        file_txt.write("--" * 40)
    file_txt.close()
    print(' ')
    print('Finish to collect data from {}'.format(url))
    print('Data saved to ', file_txt.name)


if __name__ == '__main__':
    # call main function
    create_dirs()
    kijiweni()
    ajira_portal()
