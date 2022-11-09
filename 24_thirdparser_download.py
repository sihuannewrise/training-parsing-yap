import re
import requests_cache
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urljoin

BASE_DIR = Path(__file__).parent

DOWNLOADS_URL = 'https://docs.python.org/3/download.html'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')

    pattern = r'.?pdf-a4\.zip$'

    table_tag = soup.find('table', attrs={'class': 'docutils'})
    pdf_a4_tag = table_tag.find('a', {'href': re.compile(pattern)})
    pdf_a4_link = pdf_a4_tag['href']

    archive_url = urljoin(DOWNLOADS_URL, pdf_a4_link)
    filename = archive_url.split('/')[-1]
    downloads_dir = BASE_DIR / 'downloads'
    downloads_dir.mkdir(exist_ok=True)
    archive_path = downloads_dir / filename

    response = session.get(archive_url)
    with open(archive_path, 'wb') as file:
        file.write(response.content)
