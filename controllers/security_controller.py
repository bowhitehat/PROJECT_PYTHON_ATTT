import pandas as pd
import os
from datetime import datetime

DATA_PATH = "data/raw_data.csv"


def load_data():
    return pd.read_csv(DATA_PATH, sep=";")


def save_data(df):
    df.to_csv(DATA_PATH, sep=";", index=False)


def filter_by_security_level(level):
    df = load_data()
    if level.lower() != "all":
        df = df[df["security_level"].str.lower() == level.lower()]
    return df


def delete_row(account_id):
    df = load_data()
    df = df[df["account_id"] != int(account_id)]
    save_data(df)


def clean_data():
    df = load_data()
    df = df.drop_duplicates()
    df = df.dropna()
    save_data(df)


def add_record(record: dict):
    df = load_data()
    record["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)
    save_data(df)


def update_record(account_id, new_data: dict):
    df = load_data()
    for key, value in new_data.items():
        df.loc[df["account_id"] == int(account_id), key] = value
    save_data(df)
