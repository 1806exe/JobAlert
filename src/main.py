"""
    Author: 1806exe
    Email: 1806exe@gmail.com
    GitHub: https://www.github.com/1806exe
"""

import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup


# Configuration dictionary.
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


def create_timestamped_folder_structure(website_data, base_dir="jobs"):
    """
    Creates a timestamped folder structure for the specified website data within the "jobs" folder.

    Args:
        website_data (dict): A dictionary containing website configuration data.
        base_dir (str, optional): The base directory where folders will be created. Defaults to "jobs".

    Returns:
        str: The absolute path to the newly created data folder.
    """

    timestamp = datetime.now().strftime("%Y%m%d")
    folder_prefix = website_data['folder_prefix']
    folder_name = f"{folder_prefix}_{timestamp}"
    data_folder = os.path.join(base_dir, folder_name, "data")

    try:
        os.makedirs(data_folder)
    except FileExistsError:
        print(f"Folder '{data_folder}' already exists.")

    return data_folder


def write_job_data_to_file(results, data_folder):
    """
    Writes job data extracted from website scraping to a text file.

    Args:
        results (list): A list of BeautifulSoup elements containing job data.
        data_folder (str): The absolute path to the data folder where the file will be saved.
    """

    timestamp = datetime.now().strftime("%H%M")
    file_name = f"{data_folder.split('/')[-1]}_{timestamp}.txt" 
    file_path = os.path.join(data_folder, file_name)

    with open(file_path, "a") as file:
        for element in results:
            try:
                job_a_tag = element.find("h3", class_="loop-item-title").find('a')
                if job_a_tag:
                    job_link = job_a_tag['href']
                    job_title = job_a_tag.text.strip().upper()
                    date_tag = element.find("time", class_="entry-date")
                    if date_tag:
                        job_date = date_tag['datetime']
                        file.write(f"{job_link}\n{job_title}\n{job_date}\n\n")
            except AttributeError:
                print(f"Error retrieving data from element: {element}")


def scrape_website(website_key):
    """
    Scrapes job data from a website specified by its key in the configuration dictionary.

    Args:
        website_key (str): The key in the config dictionary that identifies the website to scrape.
    """

    website_data = config[website_key]
    data_folder = create_timestamped_folder_structure(website_data)

    URL = website_data['url']
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(attrs={'class': 'loop-item-content'})

    write_job_data_to_file(results, data_folder)


if __name__ == "__main__":
    for website_key in config:
        scrape_website(website_key)