import requests
from bs4 import BeautifulSoup

# Function to scrape a Wikipedia page
def scrape_wikipedia_page(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        return soup.find_all("tab")
    else:
        print(f'Failed to retrieve page: {response.status_code}')

# Example usage
url = 'https://en.wikipedia.org/wiki/List_of_proper_names_of_stars#cite_note-IAU-LSN-1'  # Replace with the desired Wikipedia URL
scrape_wikipedia_page(url)
