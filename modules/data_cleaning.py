import pandas as pd

def load_data(path):
    df = pd.read_excel(path)
    df = df[[
        'account id',
        'Timestamp',
        'Age (*Choose the age range to which you belong)',
        'Gender',
        '1.Types of digital devices that you use on a daily basis  ( *Can choose multiple option)',
        '2. How concerned are you about your privacy online? '
    ]]
    df.columns = [
        'account_id',
        'timestamp',
        'age_range',
        'gender',
        'device',
        'privacy_concern'
    ]
    return df

def clean_data(df):
    df = df.dropna()
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.lower()
    return df

if __name__ == "__main__":
    df = load_data("data/raw_data.xlsx")
    df = clean_data(df)
    df.to_csv("data/data_clean.csv", index=False)
    print("✅ Data cleaned")
