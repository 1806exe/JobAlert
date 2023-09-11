"""
    Author: 1806exe
    Email: 1806exe@gmail.com
    GitHub: https://www.github.com/1806exe
"""


import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def create_timestamp_folder_with_data_subfolder():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    folder_name = f"jobs_{timestamp}"
    data_folder = os.path.join(folder_name, "data")

    try:
        os.makedirs(data_folder)  
    except FileExistsError:
        print(f"Jobs '{folder_name}' and 'data' subfolder already exist.")


def scrape_ajirayako():
    URL = 'https://ajirayako.co.tz/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(attrs={'class':'nextajax-item'})
    for element in results:
        job_link = element.find("a", class_="job-details-link").attrs['href']
        print(job_link)


if __name__ == "__main__":

    # create_timestamp_folder_with_data_subfolder()
    scrape_ajirayako()