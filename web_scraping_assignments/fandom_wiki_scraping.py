import requests
from bs4 import BeautifulSoup
import csv

# Set the URL for the Marvel Database characters page
url = 'https://marvel.fandom.com/wiki/Category:Characters'
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the character names (adjust selectors based on HTML structure)
characters = soup.find_all('a', class_='category-page__member-link')

# Open CSV file to write the scraped data
with open('marvel_characters.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Character Name", "Character URL"])  # Header row
    
    # Loop through the character links and write to the CSV
    for character in characters:
        name = character.text.strip()
        link = 'https://marvel.fandom.com' + character['href']
        writer.writerow([name, link])

print("Scraping complete! Data saved to marvel_characters.csv.")
