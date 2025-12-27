import pandas as pd


def load_data(path):
    # 🔥 QUAN TRỌNG: file dùng dấu ;
    df = pd.read_csv(path, sep=";")

    # Giữ đúng các cột cần dùng
    df = df[
        [
            "account_id",
            "timestamp",
            "age_range",
            "gender",
            "device",
            "loss_times",
            "loss_reason",
            "recovered",
            "security_level",
        ]
    ]

    return df


def clean_data(df):
    # Xóa dòng rỗng
    df = df.dropna()

    # Chuẩn hóa text
    text_cols = [
        "age_range",
        "gender",
        "device",
        "loss_reason",
        "recovered",
        "security_level",
    ]

    for col in text_cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.lower()
        )

    # Chuyển loss_times về số
    df["loss_times"] = df["loss_times"].astype(int)

    return df


if __name__ == "__main__":
    input_path = "data/raw_data.csv"
    output_path = "data/data_clean.csv"

    df = load_data(input_path)
    df = clean_data(df)

    df.to_csv(output_path, index=False)
    print("✅ Data cleaned successfully!")
