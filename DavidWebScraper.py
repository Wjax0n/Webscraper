import requests 
from bs4 import BeautifulSoup
import re
import schedule
import time

# Function to crawl and search for keywords on each website
def crawl_and_search(url, keywords):
    # Fetch HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()

    # Search for keywords
    matches = []
    for keyword in keywords:
        if re.search(keyword, text):
            matches.append(keyword)
    
    if matches:
        # Send email
        send_email(url, matches)

# Function to send email
def send_email(url, matches):
    # Email configurations
    from_address = 'your_email@example.com'
    to_address = 'recipient@example.com'
    subject = 'New Listings Found on {}'.format(url)
    body = 'Keywords matched: {}'.format(', '.join(matches))
    # Look into how to send email
   
def main():
    websites = {
        '秋田県警': ['売', '売払', '売却', '回転翼', '回転翼航空機', '航空'],
        # Add other websites here
    }

    for url, keywords in websites.items():
        schedule.every().day.at('08:00').do(crawl_and_search, url, keywords)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

