"""
    Author: 1806exe
    Email: 1806exe@gmail.com
    GitHub: https://www.github.com/1806exe
"""

import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# Configuration dictionary
config = {
    'ajirayako': {
        'url': 'https://ajirayako.co.tz/',
        'folder_prefix': 'ajirayako',
    },
    'mabumbe': {
        'url': 'https://mabumbe.com/jobs/',
        'folder_prefix': 'mabumbe',
    },
}

def create_timestamp_folder_with_data_subfolder(folder_prefix):
    timestamp = datetime.now().strftime("%Y%m%d")
    folder_name = f"{folder_prefix}_{timestamp}"
    data_folder = os.path.join(folder_name, "data")

    try:
        os.makedirs(data_folder)
    except FileExistsError:
        print(f"Folder '{data_folder}' already exists.")

def write_job_data_to_file(results, folder_path, folder_prefix):
    times = datetime.now().strftime("%H%M")
    file_name = f"{folder_prefix}_{times}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "a") as file:
        for element in results:
            job_a_tag = element.find("h3", class_="loop-item-title").find('a')
            job_link = job_a_tag['href']
            job_title = job_a_tag.text.strip().upper()
            date_tag = element.find("time", class_="entry-date")
            job_date = date_tag['datetime']

            file.write(f"{job_link}\n{job_title}\n{job_date}\n\n")

def scrape_website(website_key):
    website_data = config[website_key]
    create_timestamp_folder_with_data_subfolder(website_data['folder_prefix'])
    URL = website_data['url']
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(attrs={'class': 'loop-item-content'})
    current_directory = os.getcwd()
    folder_prefix = website_data['folder_prefix']
    folder_path = os.path.join(current_directory, f"{folder_prefix}_{datetime.now().strftime('%Y%m%d')}")
    os.chdir(folder_path)
    write_job_data_to_file(results, folder_path, folder_prefix)

if __name__ == "__main__":
    for website_key in config:
        scrape_website(website_key)

