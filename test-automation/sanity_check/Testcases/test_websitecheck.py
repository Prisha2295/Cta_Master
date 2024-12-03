import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import concurrent.futures

class WebsiteCrawler:
    def __init__(self, logger=None):
        self.logger = logger
        self.session = requests.Session()

    def fetch_page(self, url, timeout=30):
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            if self.logger:
                self.logger.error(f"Error fetching {url}: {e}")
            return None

    def extract_links(self, base_url, soup):
        links = set()  # Use a set to avoid duplicate URLs
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            absolute_url = urljoin(base_url, href)
            if absolute_url.startswith(base_url):  # Filter to crawl only within the base URL
                links.add(absolute_url)
        return links

    def get_seo_info(self, url, soup):
        title = soup.find('title')
        title_text = title.text if title else 'Title Not Found'

        h1_tag = soup.find('h1')
        h1_text = h1_tag.text if h1_tag else 'H1 Tag Not Found'

        status_code = requests.head(url).status_code

        description_tag = soup.find('meta', attrs={'name': 'description'})
        description_text = description_tag.get('content') if description_tag else 'Description Not Found'

        return {
            'URL': url,
            'Title': title_text,
            'H1 Tag': h1_text,
            'Status Code': status_code,
            'Description': description_text
        }

    def write_to_csv(self, filename, data):
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['URL', 'Title', 'H1 Tag', 'Status Code', 'Description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

    def crawl_website(self, base_url, max_depth, current_depth=0, writer=None):
        if current_depth > max_depth:
            return

        if self.logger:
            self.logger.info(f"Crawling {base_url} (Depth: {current_depth})")
            self.logger.info(base_url)

        html = self.fetch_page(base_url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            seo_info = self.get_seo_info(base_url, soup)
            if seo_info:
                writer.writerow(seo_info)
                if seo_info['Status Code'] != 200:
                    self.write_to_csv('status_not_200.csv', seo_info)
                if seo_info['H1 Tag'] == 'H1 Tag Not Found':
                    self.write_to_csv('missing_h1.csv', seo_info)
                if seo_info['Title'] == 'Title Not Found':
                    self.write_to_csv('missing_title.csv', seo_info)
                if seo_info['Description'] == 'Description Not Found':
                    self.write_to_csv('missing_description.csv', seo_info)

            links = self.extract_links(base_url, soup)
            with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:  # Increase workers
                futures = [executor.submit(self.crawl_website, link, max_depth, current_depth + 1, writer) for link in links]
                for future in concurrent.futures.as_completed(futures):
                    future.result()  # To raise any exceptions caught during the threads

def test_crawl_website():
    start_url = 'https://www.collegedekho.com/'
    max_depth = 2  # Reduce depth for quicker execution
    csv_filename = 'seo_results.csv'

    crawler = WebsiteCrawler()

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['URL', 'Title', 'H1 Tag', 'Status Code', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        crawler.crawl_website(start_url, max_depth, writer=writer)

    if crawler.logger:
        crawler.logger.info("Main SEO information has been saved.")
        crawler.logger.info("Additional SEO information has been saved.")

if __name__ == "__main__":
    test_crawl_website()
