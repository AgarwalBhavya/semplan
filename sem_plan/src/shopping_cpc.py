import pandas as pd

def suggest_shopping_cpc(input_csv, conversion_rate, target_cpa):
    df = pd.read_csv(input_csv)
    target_cpc = target_cpa * conversion_rate
    df['Suggested CPC'] = target_cpc
    return df[df['Top of Page Bid (Low)'] <= target_cpc]
