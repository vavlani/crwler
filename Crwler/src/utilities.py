from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os


def download_page(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
    else:
        print(f"Failed to download {url}")


def get_dir_path(parsed_main_url):
    # Ensure main_path is a directory path, not a file path
    main_path = parsed_main_url.path
    if '.' in main_path.split('/')[-1]:  # Checks if the last segment contains a file
        main_path = '/'.join(main_path.split('/')[:-1])  # Remove the file, keep as directory
    
    # Ensure main_path ends with '/'
    if not main_path.endswith('/'):
        main_path += '/'

    return main_path


