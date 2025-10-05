import requests                  # To make HTTP requests to the website
from bs4 import BeautifulSoup    # To parse HTML content
import pandas as pd              # To store data in DataFrame and export to CSV
from datetime import datetime    # To get the current date for the data

# ----------------------------
# CONFIG
# ----------------------------
keyword = "cips"  # Search term for chips (in Turkish)
base_url = "https://www.sokmarket.com.tr/arama?q=" + keyword  # Construct the search URL dynamically

# Headers to mimic a real browser, which helps avoid basic bot detection
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

# ----------------------------
# SCRAPE
# ----------------------------
# Send a GET request to the search page
response = requests.get(base_url, headers=headers)

# Check if the request was successful (HTTP 200)
if response.status_code != 200:
    print("Error fetching SOK page:", response.status_code)
    exit()  # Stop execution if page cannot be fetched

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all product cards on the page using the container div class
cards = soup.find_all("div", class_="CProductCard-module_productCardWrapper__okAmT")

# Initialize a list to store the extracted product data
data = []

# Loop through each product card and extract details
for card in cards:
    # Extract product name from the <h2> tag with the specific class
    name_tag = card.find("h2", class_="CProductCard-module_title__u8bMW")
    
    # Extract price by finding <span> tags where the style attribute contains "font-size"
    # This works because the price is displayed with font-size styling
    price_tag = card.find("span", style=lambda s: s and "font-size" in s)
    
    # Get the text content of name and price, stripping extra whitespace
    name = name_tag.get_text(strip=True) if name_tag else None
    price_text = price_tag.get_text(strip=True) if price_tag else None

    # Normalize price:
    # Convert "21,90₺" → 21.90 as a float
    price = None
    if price_text:
        price = float(price_text.replace("₺", "").replace(",", ".").strip())

    # Only append to data if both name and price exist
    if name and price:
        data.append({
            "Product Name": name,                        # Product title
            "Price": price,                              # Normalized price as float
            "Store": "SOK",                              # Store name
            "URL": base_url,                             # URL of the search page
            "Date": datetime.today().strftime("%Y-%m-%d") # Date of scraping
        })

# ----------------------------
# SAVE
# ----------------------------
# Convert the list of dictionaries to a pandas DataFrame
df_sok = pd.DataFrame(data)

# Save the DataFrame to a CSV file in UTF-8 with BOM to handle Turkish characters
df_sok.to_csv("data/sok_chips.csv", index=False, encoding="utf-8-sig")

# Print confirmation message and first few rows
print(f"✅ Scraped {len(df_sok)} items from SOK Market.")
print(df_sok.head())
