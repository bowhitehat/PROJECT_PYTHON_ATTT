import pandas as pd
import os

DATA_CLEAN_PATH = "data/data_clean.csv"
OUTPUT_DIR = "data"


def load_clean_data():
    """Load cleaned data"""
    if not os.path.exists(DATA_CLEAN_PATH):
        raise FileNotFoundError("Cleaned data not found. Run data_cleaning.py first.")
    return pd.read_csv(DATA_CLEAN_PATH)


def analyze_age_range(df):
    """Analyze age range distribution"""
    result = df["age_range"].value_counts().reset_index()
    result.columns = ["age_range", "count"]
    return result


def analyze_device_usage(df):
    """Analyze device usage frequency"""
    devices = df["device"].dropna().str.lower().str.split(",")
    device_list = []

    for row in devices:
        device_list.extend([d.strip() for d in row])

    result = pd.Series(device_list).value_counts().reset_index()
    result.columns = ["device", "count"]
    return result


def analyze_privacy_concern(df):
    """Analyze privacy concern levels"""
    result = df["privacy_concern"].value_counts().reset_index()
    result.columns = ["privacy_concern", "count"]
    return result


def save_analysis_results():
    """Run all analyses and save results"""
    df = load_clean_data()

    age_stats = analyze_age_range(df)
    device_stats = analyze_device_usage(df)
    privacy_stats = analyze_privacy_concern(df)

    age_stats.to_csv(os.path.join(OUTPUT_DIR, "age_statistics.csv"), index=False)
    device_stats.to_csv(os.path.join(OUTPUT_DIR, "device_statistics.csv"), index=False)
    privacy_stats.to_csv(os.path.join(OUTPUT_DIR, "privacy_statistics.csv"), index=False)

    return age_stats, device_stats, privacy_stats


if __name__ == "__main__":
    save_analysis_results()
    print("✅ Analysis completed. Files saved to data/")
