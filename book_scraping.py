#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://books.toscrape.com/catalogue/page-1.html"  # Adjust the URL if necessary

# Send a request to fetch the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all book containers
books = soup.find_all("article", class_="product_pod")

# List to store book data
book_data = []

# Loop through each book and extract the title and price
for book in books:
    # Extract the title
    title = book.h3.a["title"]
    
    # Extract the price
    price = book.find("p", class_="price_color").text.strip()
    
    # Add to the list as a dictionary
    book_data.append({"Title": title, "Price": price})

# Print the scraped data
for item in book_data:
    print(item)


# In[ ]:




