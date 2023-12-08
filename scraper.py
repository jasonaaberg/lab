import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
url = "https://noted.lol/"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the article elements on the page
articles = soup.find_all("article")

# Create an empty list to store the extracted information
data = []

# Iterate over each article and extract the title, URL, and image source
for article in articles:
    # Extract the title
    title = article.find("h3").text.strip()
    
    # Extract the URL
    url = article.find("a")["href"]
    
    # Extract the image source
    image_src = article.find("img")["src"]
    
    # Append the extracted information as a dictionary to the list
    data.append({"Title": title, "URL": url, "Image Source": image_src})

# Create a CSV file and write the extracted information to it
with open("articles.csv", "w", newline="") as csvfile:
    fieldnames = ["Title", "URL", "Image Source"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()  # Write the header row
    writer.writerows(data)  # Write the data rows

print("Data has been scraped and written to articles.csv.")
