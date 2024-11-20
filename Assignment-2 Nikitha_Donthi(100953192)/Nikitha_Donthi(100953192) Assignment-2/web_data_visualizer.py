# Name: Nikitha Donthi (100953192)
# Date: 15-11-2024


import requests
from bs4 import BeautifulSoup
import csv

# Input URL and file name
url = input("Enter the URL of the website to scrape: ") # Example Url in output I used: https://books.toscrape.com/ 
filename = input("Enter the filename to save data (e.g., data.csv): ")

print("\nFetching data...")
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extract book titles and prices
    items = soup.find_all('article', class_='product_pod')
    if not items:
        print("No valid data extracted. Please check the website URL or structure.")
        exit()

    data = []
    for item in items:
        title = item.h3.a['title']
        price = item.find('p', class_='price_color').text
        data.append({'Title': title, 'Price': price})

    # Save to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Price'])
        writer.writeheader()
        writer.writerows(data)

    print(f"Data successfully extracted and saved to {filename}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the website: {e}")
