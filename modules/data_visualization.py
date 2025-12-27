import sys
import os

# thêm root project vào PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
import matplotlib.pyplot as plt

# ===== CONSTANTS =====
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)   # 🔥 tự tạo thư mục images nếu chưa có

def plot_csv(path, title, xlabel, output_name, show=False):
    df = pd.read_csv(path)

    plt.figure(figsize=(9,5))
    plt.bar(df.iloc[:, 0], df.iloc[:, 1])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_path = os.path.join(IMAGE_DIR, output_name)
    plt.savefig(output_path)   # ✅ LƯU FILE
    print(f"✅ Saved chart: {output_path}")

    if show:
        plt.show()
    else:
        plt.close()

# ===== RUN =====
if __name__ == "__main__":
    plot_csv(
        "data/loss_reason_statistics.csv",
        "Loss Reason Distribution",
        "Loss Reason",
        "loss_reason_chart.png"
    )

    plot_csv(
        "data/device_statistics.csv",
        "Device Usage",
        "Device",
        "device_chart.png"
    )

    plot_csv(
        "data/security_level_statistics.csv",
        "Security Level",
        "Security Level",
        "security_level_chart.png"
    )
