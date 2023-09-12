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
    timestamp = datetime.now().strftime("%Y%m%d")
    folder_name = f"jobs_{timestamp}"
    # data_folder = os.path.join(folder_name, "data")

    try:
        os.makedirs(folder_name)  
    except FileExistsError:
        print(f"Jobs '{folder_name}' and 'data' subfolder already exist.")


def scrape_ajirayako():
    create_timestamp_folder_with_data_subfolder()
    URL = 'https://ajirayako.co.tz/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(attrs={'class':'nextajax-item'})
    times = datetime.now().strftime("%H%M") 
    file_name = f"ajirayako_{times}.txt"
    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, 'jobs_{0}'.format(datetime.now().strftime("%Y%m%d")))
    file_path = os.path.join(folder_path, file_name)
    os.chdir(folder_path)  
    for element in results:
        job_link = element.find("a", class_="job-details-link").attrs['href']
        job_title = element.find("h3", class_="loop-item-title").text
        job_date = element.find("span", class_="job-date").text 
        with open(file_path, "a") as file:
            file.write('{0}\n'.format(job_link.strip()))
            file.write('{0}\n'.format(job_title.strip().upper()))
            file.write('{0}\n'.format(job_date.strip()))
            file.write('\n')    


if __name__ == "__main__":

    # create_timestamp_folder_with_data_subfolder()
    scrape_ajirayako()