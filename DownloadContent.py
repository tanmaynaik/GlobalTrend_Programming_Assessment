""" Write a Python function that takes a list of URLs, 
attempts to download their content, and retries up to 3 times
if an error occurs. Use appropriate error handling 
to manage different types of exceptions. """

import requests
from time import sleep

def download_content(urls, max_retries=3):
    results = {}
    
    for url in urls:
        attempts = 0
        success = False
        
        while attempts < max_retries and not success:
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
                results[url] = response.text
                success = True
            except requests.exceptions.HTTPError as e:
                print(f"HTTP error for {url}: {e}")
            except requests.exceptions.ConnectionError as e:
                print(f"Connection error for {url}: {e}")
            except requests.exceptions.Timeout as e:
                print(f"Timeout error for {url}: {e}")
            except requests.exceptions.RequestException as e:
                print(f"Request error for {url}: {e}")
            except Exception as e:
                print(f"Unexpected error for {url}: {e}")
            
            attempts += 1
            if not success:
                sleep(1)  # Wait a bit before retrying
        
        if not success:
            results[url] = None  # Indicate that the download failed after all retries
    
    return results

# Example usage
urls = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://wikipedia.com"
]
content = download_content(urls)
for url, text in content.items():
    if text:
        print(f"Content for {url}:\n{text[:100]}...\n")
    else:
        print(f"Failed to download content for {url}\n")
