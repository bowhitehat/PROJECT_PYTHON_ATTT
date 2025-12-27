import pandas as pd
import matplotlib.pyplot as plt
import os

# ================== CẤU HÌNH CHUNG ==================
plt.rcParams['font.family'] = 'DejaVu Sans'   # Hỗ trợ tiếng Việt
plt.rcParams['axes.unicode_minus'] = False   # Fix lỗi dấu âm

IMG_DIR = "images"
os.makedirs(IMG_DIR, exist_ok=True)

df = pd.read_csv("data/data_clean.csv")

# ================== BIỂU ĐỒ ==================

def plot_age_distribution():
    plt.figure(figsize=(8, 5))
    df['age_range'].value_counts().plot(kind='bar')
    plt.title("Phân bố độ tuổi")
    plt.xlabel("Độ tuổi")
    plt.ylabel("Số lượng")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f"{IMG_DIR}/age_distribution.png")
    plt.close()


def plot_gender_ratio():
    plt.figure(figsize=(6, 6))
    df['gender'].value_counts().plot(
        kind='pie',
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title("Tỉ lệ Nam / Nữ")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(f"{IMG_DIR}/gender_ratio.png")
    plt.close()


def plot_device_usage():
    plt.figure(figsize=(9, 5))
    df['device'].str.split(', ').explode().value_counts().plot(kind='bar')
    plt.title("Thiết bị sử dụng")
    plt.xlabel("Thiết bị")
    plt.ylabel("Số lượng")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f"{IMG_DIR}/device_usage.png")
    plt.close()


def plot_security_level():
    plt.figure(figsize=(7, 5))
    df['security_level'].value_counts().plot(kind='bar')
    plt.title("Mức độ an toàn")
    plt.xlabel("Security level")
    plt.ylabel("Số lượng")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f"{IMG_DIR}/security_level.png")
    plt.close()

def plot_loss_reason():
    data = df.copy()

    # Chuẩn hóa dữ liệu
    data["loss_reason"] = data["loss_reason"].fillna("unknown").str.lower()

    counts = data["loss_reason"].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=140
    )
    plt.title("Tỉ lệ nguyên nhân mất tài khoản")

    plt.tight_layout()
    plt.savefig(f"{IMG_DIR}/loss_reason.png")
    plt.close()



# ================== CHẠY TẤT CẢ ==================

if __name__ == "__main__":
    plot_age_distribution()
    plot_gender_ratio()
    plot_device_usage()
    plot_security_level()
    plot_loss_reason()
    print("✅ Đã tạo toàn bộ biểu đồ")
