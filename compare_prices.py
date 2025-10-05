import pandas as pd
from rapidfuzz import process, fuzz
import os

# Create data folder if missing
os.makedirs("data", exist_ok=True)

# Load CSV files
a101_file = "data/a101_chips.csv"
sok_file = "data/sok_chips.csv"

a101_df = pd.read_csv(a101_file)
sok_df = pd.read_csv(sok_file)

# Standardize column names for consistency
a101_df.rename(columns={'name': 'name', 'price': 'price'}, inplace=True)
sok_df.rename(columns={'Product Name': 'name', 'Price': 'price'}, inplace=True)

# Normalize product names for matching
def normalize_name(name):
    return str(name).lower().strip()

a101_df['name_norm'] = a101_df['name'].apply(normalize_name)
sok_df['name_norm'] = sok_df['name'].apply(normalize_name)

# Match similar products using fuzzy string matching
matches = []

for a101_index, a101_row in a101_df.iterrows():
    match_name, score, sok_index = process.extractOne(
        a101_row['name_norm'], 
        sok_df['name_norm'], 
        scorer=fuzz.token_sort_ratio
    )
    if score >= 70:  # similarity threshold
        sok_row = sok_df.loc[sok_index]
        matches.append({
            'product_name': a101_row['name'],
            'a101_price': a101_row['price'],
            'sok_price': sok_row['price'],
            'cheapest_store': 'A101' if a101_row['price'] < sok_row['price'] else 'Sok'
        })

# Save comparison CSV
comparison_df = pd.DataFrame(matches)
output_file = "data/compare_chips.csv"
comparison_df.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"✅ Comparison saved to '{output_file}'")
print(comparison_df.head())
