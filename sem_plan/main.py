from src.keyword_scraper import scrape_website_text
from src.keyword_filter import filter_keywords
from src.pmax_themes import generate_pmax_themes
from src.shopping_cpc import suggest_shopping_cpc

# Example usage:
brand_url = "https://www.myprotein.com/"
competitor_url = "https://www.optimumnutrition.com/en-us"

# 1. Scrape content
brand_text = scrape_website_text(brand_url)
competitor_text = scrape_website_text(competitor_url)

# 2. Filter keywords
filter_keywords("data/keyword_raw.csv", "data/keyword_filtered.csv")

# 3. Generate PMax themes
grouped_keywords = "protein powder, vegan protein, buy supplements"
themes = '''
Product Category Themes:
- Vegan Protein
- Post-Workout Drinks

Use-case Themes:
- Muscle Gain
- Weight Loss

Demographics:
- For Working Professionals
- For Athletes

Seasonal Themes:
- New Year Fitness
- Summer Body Ready
'''
with open("outputs/pmax_themes.txt", "w") as f:
     f.write(themes)

# 4. Suggest CPC for Shopping ads
df_cpc = suggest_shopping_cpc("data/keyword_filtered.csv", 0.02, 20)
df_cpc.to_csv("outputs/shopping_cpc_suggestions.csv", index=False)
from src.ad_group_generator import generate_ad_groups
generate_ad_groups("data/keyword_filtered.csv", "outputs/ad_groups.json")

