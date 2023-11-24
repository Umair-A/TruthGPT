import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def google_search(query, api_key, cse_id, **kwargs):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'cx': cse_id,
        'key': api_key,
    }
    params.update(kwargs)
    response = requests.get(search_url, params=params)
    return response.json()

def extract_snippet(results):
    if 'items' in results:
        for item in results['items']:
            print(item['title'])
            print(item['snippet'])
            print(item['link'])
            print("\n")

def main():
    api_key = os.getenv("api_key")  # Replace with your actual API key
    cse_id = os.getenv("cse_id")   # Your Custom Search Engine ID

    query = input("Query: ")
    results = google_search(query, api_key, cse_id, num=3)
    extract_snippet(results)

if __name__ == '__main__':
    main()
