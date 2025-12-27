import pandas as pd

df = pd.read_csv("data/data_clean.csv")

df['age_range'].value_counts().reset_index() \
    .rename(columns={'index':'age_range', 'age_range':'count'}) \
    .to_csv("data/age_statistics.csv", index=False)

df['privacy_concern'].value_counts().reset_index() \
    .rename(columns={'index':'privacy_concern', 'privacy_concern':'count'}) \
    .to_csv("data/privacy_statistics.csv", index=False)

df['device'].str.split(',').explode().str.strip() \
    .value_counts().reset_index() \
    .rename(columns={'index':'device', 'device':'count'}) \
    .to_csv("data/device_statistics.csv", index=False)

print("✅ Analysis completed")
