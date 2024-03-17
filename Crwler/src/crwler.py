import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
from utilities import download_page, get_dir_path

def extract_links(url, main_url_netloc, main_url_dir_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = set()

    for link in soup.find_all('a', href=True):
        href = link['href']
        parsed_href = urlparse(href)

        # Ignore the fragment portion of the URL
        clean_href = parsed_href._replace(fragment="").geturl()

        if parsed_href.scheme in ['http', 'https']:
            if parsed_href.netloc == main_url_netloc and parsed_href.path.startswith(main_url_dir_path):
                links.add(clean_href)
        elif not parsed_href.scheme:  # Likely a relative link
            absolute_url = urljoin(url, clean_href)
            parsed_absolute_url = urlparse(absolute_url)
            if urlparse(absolute_url).netloc == main_url_netloc and parsed_absolute_url.path.startswith(main_url_dir_path):
                links.add(absolute_url)
        # Other schemes like 'javascript:', 'mailto:', etc., are ignored

    return links


def crawl_website(main_url, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    main_url_netloc = urlparse(main_url).netloc
    main_url_dir_path = get_dir_path(urlparse(main_url))

    print(f'\n{main_url_dir_path}\n')
    
    to_download = {main_url}
    downloaded = set()

    while to_download:
        url = to_download.pop()
        if url in downloaded:
            continue

        print(f"Downloading: {url}")
        file_name = url.split('/')[-1] or "index.html"
        file_path = os.path.join(output_dir, file_name)
        download_page(url, file_path)

        for link in extract_links(url, 
                                  main_url_netloc, 
                                  main_url_dir_path):
            # print(f'downloaded link: {link}')
            if link not in downloaded:
                to_download.add(link)

        downloaded.add(url)
    
    return downloaded


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Crwler: Web Crawler for Hierarchical Site Mapping.')
    parser.add_argument('--url', required=True, help='Base URL to start crawling from')
    parser.add_argument('--output_dir', required=True, help='Absolute folder path for downloaded files')
    args = parser.parse_args()
    crawl_website(args.url, args.output_dir)

