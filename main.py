import os
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from urllib.parse import urlparse

class PendekarLaut:
    def __init__(self, main_url):
        self.main_url = main_url

    def get_content(self, url):
        try:
            headers = Headers().generate()
            r = requests.get(url=url, headers=headers)
            if r.status_code == 200:
                return r.text
        except Exception as err:
            return err

    def get_images(self, content, url):
        soup = BeautifulSoup(content, 'html.parser')
        img_tags = soup.find_all('img')
        image_urls = [img['src'] for img in img_tags]
        unique_img_urls = list(set(image_urls))
        return unique_img_urls

    def download_images(self, image_urls, folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        for img_url in image_urls:
            img_name = os.path.basename(urlparse(img_url).path)
            img_path = os.path.join(folder_name, img_name)
            try:
                with open(img_path, 'wb') as f:
                    img_content = requests.get(img_url).content
                    f.write(img_content)
                print(f"Image saved: {img_path}")
            except Exception as e:
                print(f"Failed to save image: {img_url}, Error: {e}")

    def get_all_episode(self):
        content = self.get_content(self.main_url)
        soup = BeautifulSoup(content, 'html.parser')
        selected_element = soup.select('.list-label-widget-content > div > ul > li')
        href_list = []
        for element in selected_element:
            href = element.a.get('href')
            if href:
                href_list.append(href)
        return href_list

    def read_more_url(self, url):
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        a_tags = soup.find_all('a')
        for a_tag in a_tags:
            if "Read more" in a_tag.get_text(strip=True):
                read_more_href = a_tag.get('href')
                return read_more_href
        return None

    def scrape_comics(self):
        episodes = self.get_all_episode()
        for e in episodes:
            url = self.read_more_url(e)
            folder_name = urlparse(url).path.strip('/').split('/')[-1]
            content = self.get_content(url)
            image_urls = self.get_images(content, url)
            self.download_images(image_urls, folder_name)

if __name__ == "__main__":
    MAIN_URL = 'https://plkomikhk.blogspot.com/'
    scraper = PendekarLaut(MAIN_URL)
    scraper.scrape_comics()
