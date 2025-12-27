import pandas as pd
import os


DATA_PATH = "data/data_clean.csv"
OUTPUT_DIR = "data"


def load_clean_data():
    return pd.read_csv(DATA_PATH)


def explode_devices(df):
    df = df.copy()
    df["device"] = df["device"].str.split(",")
    return df.explode("device")


# ================== ANALYSIS FUNCTIONS ==================
def analyze_device_usage(df):
    df = explode_devices(df)
    stats = (
        df["device"]
        .str.strip()
        .value_counts()
        .reset_index()
    )
    stats.columns = ["device", "count"]
    return stats


def analyze_security_level(df):
    stats = (
        df["security_level"]
        .value_counts()
        .reset_index()
    )
    stats.columns = ["security_level", "count"]
    return stats


def analyze_loss_reason(df):
    stats = (
        df["loss_reason"]
        .value_counts()
        .reset_index()
    )
    stats.columns = ["loss_reason", "count"]
    return stats


def analyze_gender(df):
    stats = (
        df["gender"]
        .value_counts()
        .reset_index()
    )
    stats.columns = ["gender", "count"]
    return stats


# ================== SAVE RESULTS ==================
def save_analysis():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df = load_clean_data()

    analyze_device_usage(df).to_csv(
        f"{OUTPUT_DIR}/device_statistics.csv", index=False
    )

    analyze_security_level(df).to_csv(
        f"{OUTPUT_DIR}/security_level_statistics.csv", index=False
    )

    analyze_loss_reason(df).to_csv(
        f"{OUTPUT_DIR}/loss_reason_statistics.csv", index=False
    )

    analyze_gender(df).to_csv(
        f"{OUTPUT_DIR}/gender_statistics.csv", index=False
    )

    print("✅ Analysis completed & CSV files saved!")


# ================== RUN ==================
if __name__ == "__main__":
    save_analysis()
