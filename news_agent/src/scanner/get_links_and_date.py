import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
from datetime import datetime, timedelta
from dateutil.parser import parse as parse_date


def scrape_links_and_dates(url: str, max_links: int = 10):
    """
    Scrape article links from a webpage and filter by published dates during scanning.
    Only includes articles published today or yesterday.
    Args:
        url (str): The URL of the webpage to scrape.
        max_links (int): Maximum number of article links to process.
    Returns:
        list: A list of dictionaries containing link.
    """
    try:
        # Calculate the date threshold (start of yesterday)
        yesterday = (datetime.now() - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        
        # Scrape the main page
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Process article links with immediate date filtering
        results = []
        processed_links = set()
        
        for a_tag in soup.find_all('a', href=True):
            # Stop if we've reached max_links
            if len(results) >= max_links:
                break
                
            href = a_tag['href']
            full_url = urljoin(url, href)
            
            # Basic URL validation
            if not (full_url.startswith(('http://', 'https://')) and
                    '#' not in full_url and
                    'vnexpress.net' in full_url and
                    re.search(r'-\d+\.html$', full_url)):
                continue
            
            # Skip if already processed
            if full_url in processed_links:
                continue
            processed_links.add(full_url)
            
            # Immediately check the article's published date
            try:
                article_response = requests.get(full_url, timeout=10)
                article_response.raise_for_status()
                article_soup = BeautifulSoup(article_response.text, 'html.parser')

                # Try extracting date from <span class="date">
                date_span = article_soup.find('span', class_='date')
                if date_span:
                    date_text = date_span.get_text(strip=True)
                    # Remove day of the week and extra text
                    cleaned_date = re.sub(r'^(Thứ\s*(hai|ba|tư|năm|sáu|bảy)|(Chủ nhật),?\s*)|\s*\(GMT\+7\)$', '', date_text).strip()
                    parsed_date = parse_date(cleaned_date)
                    
                    # Only add to results if date is from yesterday or today
                    if parsed_date >= yesterday:
                        results.append({'link': full_url})

            except requests.RequestException as e:
                results.append({'link': full_url, 'error': f'Failed to fetch article: {str(e)}'})

        return results

    except requests.RequestException as e:
        return [{'error': f'Failed to fetch the main page: {str(e)}'}]


def main():
    url = "https://vnexpress.net/khoa-hoc-cong-nghe"
    links = scrape_links_and_dates(url, 5)
    print(links)
    

if __name__ == "__main__":
    main()