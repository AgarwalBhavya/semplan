import pandas as pd
import json


def generate_ad_groups(input_csv, output_json):
    df = pd.read_csv(input_csv)

    # Match type suggestion logic (simple rule-based)
    def suggest_match_type(keyword):
        if len(keyword.split()) == 1:
            return "Exact"
        elif len(keyword.split()) == 2:
            return "Phrase"
        else:
            return "Broad"

    ad_groups = {
        "Brand Terms": [],
        "Category Terms": [],
        "Competitor Terms": [],
        "Location-based Queries": [],
        "Long-Tail Informational Queries": []
    }

    for _, row in df.iterrows():
        keyword = row['Keyword']
        match_type = suggest_match_type(keyword)
        cpc_range = [row['Top of Page Bid (Low)'], row['Top of Page Bid (High)']]

        entry = {
            "keyword": keyword,
            "match_type": match_type,
            "suggested_cpc": cpc_range
        }

        kw_lower = keyword.lower()
        if "brand" in kw_lower:
            ad_groups["Brand Terms"].append(entry)
        elif "competitor" in kw_lower:
            ad_groups["Competitor Terms"].append(entry)
        elif any(city in kw_lower for city in ["delhi", "mumbai", "bangalore"]):
            ad_groups["Location-based Queries"].append(entry)
        elif len(keyword.split()) >= 4:
            ad_groups["Long-Tail Informational Queries"].append(entry)
        else:
            ad_groups["Category Terms"].append(entry)

    with open(output_json, "w") as f:
        json.dump(ad_groups, f, indent=2)
