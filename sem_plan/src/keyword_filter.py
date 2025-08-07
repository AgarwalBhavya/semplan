import pandas as pd

def filter_keywords(input_csv, output_csv, min_search_volume=500):
    df = pd.read_csv(input_csv)
    df_filtered = df[df['Avg. Monthly Searches'] >= min_search_volume]
    df_filtered.to_csv(output_csv, index=False)
