import requests
import pandas as pd
import os

# URL of A101 search API for chips
SEARCH_URL = "https://a101.wawlabs.com/search?q=cips&pn=1&rpp=60&filter=available:true&filter=locations^location:VS032-SLOT"
OUTPUT_FILE = "data/a101_chips.csv"

# Create 'data' folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/140.0.7339.208 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
}

# Send GET request to fetch JSON
response = requests.get(SEARCH_URL, headers=headers)

if response.status_code == 200:
    data = response.json()  # Parse JSON response
    items = data.get("res", [])[0].get("page_content", [])  # Extract products

    if not items:
        print("⚠️ No products found in JSON response.")
    else:
        products = []
        for item in items:
            # Extract product info
            products.append({
                "name": item.get("title", ""),
                "price": item.get("price", ""),
                "old_price": item.get("old_price", ""),
                "category": item.get("category", "")
            })

        # Convert to DataFrame and save CSV
        df = pd.DataFrame(products)
        df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
        print(f"✅ Saved {len(df)} products to {OUTPUT_FILE}")
else:
    print(f"❌ Failed to fetch data. Status: {response.status_code}")
