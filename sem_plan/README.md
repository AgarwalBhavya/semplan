# SEM Campaign Planner

## Overview
This project helps generate a full-funnel SEM plan using:
- Google Keyword Planner data
- Brand & competitor website content
- AI (GPT-4) for theme suggestions

## Features
- Keyword scraping and filtering
- Ad group segmentation
- PMax campaign theme generation
- Shopping Ads CPC recommendations

## How to Use
1. Populate `data/keyword_raw.csv` with keyword planner data.
2. Add brand and competitor website URLs in `main.py`.
3. Insert your OpenAI API key.
4. Run: `python main.py`

## Output
- Filtered keywords: `data/keyword_filtered.csv`
- Grouped ad themes: `outputs/pmax_themes.txt`
- Shopping CPC suggestions: `outputs/shopping_cpc_suggestions.csv`
