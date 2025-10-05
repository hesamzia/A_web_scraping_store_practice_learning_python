# Chips Price Comparison: A101 vs Şok (Educational Web Scraping Project)

## Attention : 
Legality & Risk
- Web scraping can be restricted by **website terms of service**.  
- Always check `robots.txt` and site policies before scraping.  
- This project is **educational only**:
  - Scrapes only a limited number of products (≤60).  
  - Results are stored locally for learning purposes.  
  - No commercial use or repeated high-frequency scraping.  

**Risks**: Sites may block your IP if scraping is excessive. Legal consequences are unlikely for small-scale educational scraping but **should always respect website policies**.

---

## 1️⃣ What is Web Scraping?

**Web Scraping** is the process of automatically extracting information from websites. Instead of manually visiting pages and copying data, a program can access the site, read its content, and save it in a structured format (CSV, JSON, database, etc.).

---

## 2️⃣ Why We Do Web Scraping

Web scraping is useful for:

- Collecting product prices for comparison.  
- Monitoring stock or promotions.  
- Gathering datasets for analysis or educational purposes.  
- Automating repetitive tasks that involve data collection.

> In this project, the goal is to **collect chips prices from two popular Turkish stores (A101 and Şok)** and compare them for the same products.

---

## 3️⃣ Problem Definition

**Title:** Compare prices of chips products between A101 and Şok.

**Plan & Steps:**

1. Scrape products from **A101** using their JSON API endpoint.  
2. Scrape products from **Şok** using HTML scraping.  
3. Normalize product names for consistency.  
4. Match similar products using fuzzy string matching.  
5. Compare prices and determine the cheapest store.  
6. Save results to a CSV for easy analysis.

**Libraries Used:**

- `requests` — for sending HTTP requests.  
- `BeautifulSoup4 (bs4)` — for HTML parsing (Şok).  
- `pandas` — for data manipulation and CSV handling.  
- `rapidfuzz` — for fuzzy string matching (finding similar product names).  
- `os` — for handling directories and file paths.

---

## 4️⃣ HTML Scraping vs API Scraping

| Method | Definition | Use Case |
|--------|------------|----------|
| HTML Scraping | Extracts data directly from a website’s HTML structure (tags, classes, ids). | When the site does not have a public API or the API is protected. |
| API Scraping | Uses a website’s JSON or REST API endpoints to get structured data. | Faster and more reliable if a site provides an API. |

**In this project:**

- **Şok**: HTML scraping — Let's show this method.  
- **A101**: API scraping — JSON API is available and easier to parse.

---

## 5️⃣ User Manual: How to Use the Python Files

### 1️⃣ Scraping A101
Call : python a101_scraper.py
- Fetches chips products from A101’s JSON API.
- Saves results to data/a101_chips.csv.

### 2️⃣ Scraping Şok
Call : python sok_scraper.py
- Scrapes chips products from Şok’s website HTML.
- Saves results to data/sok_chips.csv.

### 3️⃣ Comparing Prices
Call : python compare_prices.py
- Loads a101_chips.csv and sok_chips.csv.
- Normalizes product names and matches similar products.
- Creates data/compare_chips.csv with:
    - Product name
    - A101 price
    - Şok price
    - Cheapest stor

## 6️⃣ Results

After running the scraping scripts:

- **A101**: 60 chips products scraped successfully (with price, old price, and category).  
- **Şok**: 20 chips products scraped successfully from HTML page (name, price, store, URL, date).  
- **Comparison**: Products with similar names are matched, and the cheapest store is highlighted in `data/compare_chips.csv`.

---