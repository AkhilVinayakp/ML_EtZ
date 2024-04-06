import time
import requests
from tqdm import tqdm

# Function to simulate sending a request
def send_request(url):
    # Simulate sending a request
    response = requests.get(url)
    time.sleep(0.5)  # Simulate processing time
    return response.status_code

# List of URLs to send requests to
urls = [
    'https://www.example.com',
    'https://www.google.com',
    'https://www.facebook.com'
]

# Create a tqdm progress bar for sending requests
with tqdm(total=len(urls), desc='Sending Requests') as pbar:
    # Iterate over each URL
    for url in urls:
        # Update the progress bar
        pbar.update(1)
        # Send the request and log the response
        status_code = send_request(url)
        print(f'Request to {url} - Status code: {status_code}')

print("All requests sent successfully.")
