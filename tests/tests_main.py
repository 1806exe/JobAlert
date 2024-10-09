import unittest
from unittest.mock import patch, Mock
import os
import requests
import sys  
from datetime import datetime
from bs4 import BeautifulSoup
from ..src import create_timestamped_folder_structure, write_job_data_to_file, scrape_website

class TestScraper(unittest.TestCase):
    @patch('requests.get')
    def test_scrape_website_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'<html><body><div class="loop-item-content"><h3 class="loop-item-title"><a href="https://example.com">Job Title</a></h3><time class="entry-date" datetime="2024-10-09">2024-10-09</time></div></body></html>'

        scrape_website('ajirayako')

        self.assertTrue(os.path.exists('jobs/ajirayako_20241009/data/ajirayako_20241009_1329.txt'))

    @patch('requests.get')
    def test_scrape_website_failure(self, mock_get):
        mock_get.return_value.status_code = 404

        with self.assertRaises(Exception):
            scrape_website('ajirayako')

    @patch('os.makedirs')
    def test_create_timestamped_folder_structure_success(self, mock_makedirs):
        website_data = {'folder_prefix': 'ajirayako'}
        create_timestamped_folder_structure(website_data)

        mock_makedirs.assert_called_once_with('jobs/ajirayako_20241009/data')

    @patch('os.makedirs')
    def test_create_timestamped_folder_structure_failure(self, mock_makedirs):
        mock_makedirs.side_effect = FileExistsError

        website_data = {'folder_prefix': 'ajirayako'}
        create_timestamped_folder_structure(website_data)

        mock_makedirs.assert_called_once_with('jobs/ajirayako_20241009/data')

    def test_write_job_data_to_file_success(self):
        results = [BeautifulSoup('<div class="loop-item-content"><h3 class="loop-item-title"><a href="https://example.com">Job Title</a></h3><time class="entry-date" datetime="2024-10-09">2024-10-09</time></div>', 'html.parser')]
        data_folder = 'jobs/ajirayako_20241009/data'
        write_job_data_to_file(results, data_folder)

        self.assertTrue(os.path.exists(f'{data_folder}/ajirayako_20241009_1329.txt'))

    def test_write_job_data_to_file_empty_results(self):
        results = []
        data_folder = 'jobs/ajirayako_20241009/data'
        write_job_data_to_file(results, data_folder)

        self.assertTrue(os.path.exists(f'{data_folder}/ajirayako_20241009_1329.txt'))
        self.assertTrue(os.stat(f'{data_folder}/ajirayako_20241009_1329.txt').st_size == 0)

if __name__ == '__main__':
    unittest.main()