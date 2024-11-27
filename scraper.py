import requests
from bs4 import BeautifulSoup
import csv

base_url = 'https://yellotalk.co/yell/'

# Define the range of numbers you want to scrape
start_number =   # Starting number
end_number =    # End number (exclusive)


#headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#
#}

#headers = {
#    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
#}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'
}

# Open a CSV file to write the output
with open('yellowtalk_31102024.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['url', 'data', 'like'])  # Write header row

    for number in range(start_number, end_number):
        url = f'{base_url}{number}'
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses

            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all <p> elements
            paragraph_elements = soup.find_all('h1')
            
            # Find all <span> elements with the class 'post-symbols'
            span_elements = soup.find_all('span', class_='post-symbols')

            # Collect text data from <p> elements
            text_data = ' '.join([element.get_text().strip() for element in paragraph_elements])
            
            # Collect text from <span> elements for likes
            likes_data = ' '.join([element.get_text().strip() for element in span_elements])
            
            # Write the URL, combined text data, and likes data to the CSV
            csv_writer.writerow([url, text_data, likes_data])

        except requests.exceptions.RequestException as e:
            print(f'Error fetching {url}: {e}')