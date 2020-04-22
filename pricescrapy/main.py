'''
This is the main module.

Specific scrapers are imported in from the scrapers module.
'''

import requests
from bs4 import BeautifulSoup

def main():
    '''Entry point into the script.'''
    url: str = 'https://google.com'
    page = requests.get(url)
    parsed = BeautifulSoup(page.content, 'html.parser')
    results = parsed.find('body')
    print(results)
