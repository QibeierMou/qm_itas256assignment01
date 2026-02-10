import time 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def fetch_with_requests(url):
    """Fetch page with requests. Returns HTML string or None."""
    try:
        response = requests.get(url , timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e :
        print(f"Requests error for {url}: {e}")
        return None
    
def fetch_with_selenium(url):
    """Fetch page with Selenium. Returns HTML string or None."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(3) 
        return driver.page_source
    finally:
        driver.quit()

def scrape_site(url, parse_function, site_name, max_jobs=15):
    """
    Scrape a site using the smart fallback approach:
    1. Try requests first
    2. Parse and check if jobs found
    3. If no jobs, retry with Selenium
    4. Return list of job dicts
    """
    print(f'\nscraping {site_name} site')
    html = fetch_with_requests(url)
    
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        jobs = parse_function(soup, max_jobs)
        if jobs:
            print(f'{site_name}: scraped using requests')

    print(f"{site_name}: falling back to Selenium")

    html = fetch_with_selenium(url)
    soup = BeautifulSoup(html, "lxml")
    return parse_function(soup, max_jobs)