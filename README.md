
# 🔐 Account Security Dashboard (Python – Tkinter)

## 👥 THÀNH VIÊN NHÓM

### 🔹 Thành viên 1

* **Họ và tên:** Trang Sĩ Hoàng
* **MSSV:** 24162035
* **Vai trò:**

  * Code giao diện GUI (Tkinter)
  * Xây dựng chức năng CRUD dữ liệu CSV
  * **Leader – Quản lý dự án**
  * Lên kế hoạch, phân công và điều phối nhóm

### 🔹 Thành viên 2

* **Họ và tên:** Hoàng Phúc Khang
* **MSSV:** 24162056
* **Vai trò:**

  * Code chức năng làm sạch dữ liệu
  * Thống kê, sắp xếp dữ liệu
  * Xử lý và chuẩn hóa dữ liệu đầu vào

### 🔹 Thành viên 3

* **Họ và tên:** Vũ Trọng Hưng
* **MSSV:** 24162053
* **Vai trò:**

  * Code chức năng trực quan hóa dữ liệu
  * Vẽ biểu đồ (Bar chart, Pie chart, Histogram)
  * Phân tích dữ liệu và thống nhất format dữ liệu
  * Làm bài báo cáocáo

### 🔹 Thành viên 4

* **Họ và tên:** Đinh Phạm Thế Khang
* **MSSV:** 24162055
* **Vai trò:**

  * Hỗ trợ kiểm thử (Testing)
  * Kiểm tra chức năng CRUD & Visualization
  * Hoàn thiện báo cáo và tài liệu
  * Làm slide thuyết trình

---

## 📁 CẤU TRÚC THƯ MỤC ĐỒ ÁN

```text
PROJECT_PYTHON/
│
├── data/
│   ├── raw_data.csv
│   ├── data_clean.csv
│   ├── loss_reason_statistics.csv
│   ├── device_statistics.csv
│   └── security_level_statistics.csv
│
├── modules/
│   ├── __init__.py
│   ├── data_cleaning.py
│   ├── account_analysis.py
│   └── data_visualization.py
│
├── views/
│   ├── assets/
│   │   ├── logo_fit.png
│   │   ├── logo_ute.png
│   │   └── bg_home.png
│   │
│   ├── auth/
│   │   ├── login_view.py
│   │   └── signup_view.py
│   │
│   ├── dashboard/
│   │   ├── home_view.py
│   │   ├── security_view.py
│   │   └── analysis_view.py
│
├── images/
│   ├── age_distribution.png
│   ├── device_usage.png
│   ├── gender_ratio.png
│   ├── security_level.png
│   └── loss_reason.png
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 GIỚI THIỆU ỨNG DỤNG

**Account Security Dashboard** là ứng dụng Python sử dụng **Tkinter**, cho phép:

* 📂 Quản lý các sự cố mất tài khoản bằng file CSV
* ✏️ Thêm, cập nhật, xóa và làm sạch dữ liệu
* 📊 Phân tích dữ liệu người dùng bị mất tài khoản
* 📈 Trực quan hóa dữ liệu bằng biểu đồ
* 🖼️ Giao diện thân thiện, có logo **FIT & UTE**

> ⚠️ Ứng dụng tập trung vào **xử lý dữ liệu – trực quan hóa – CRUD**,
> không triển khai hệ thống phân quyền người dùng.

---

## ⚙️ HƯỚNG DẪN CÀI ĐẶT & CHẠY ỨNG DỤNG

### 🔹 Cách 1: Cài đặt thư viện thủ công (Khuyến nghị)

#### Bước 1: Clone / tải source code

```bash
git clone https://github.com/bowhitehat/PROJECT_PYTHON_ATTT.git
cd PROJECT_PYTHON_ATTT
```

#### Bước 2: Cài đặt thư viện

```bash
pip install pandas
pip install matplotlib
pip install pillow
```

> ⚠️ **Tkinter** thường đã có sẵn trong Python

#### Bước 3: Chạy chương trình

---

## 🖥️ CÁCH SỬ DỤNG ỨNG DỤNG

### 🔐 Đăng nhập

* Người dùng đăng nhập để truy cập hệ thống
* Sau khi đăng nhập sẽ vào trang **Dashboard**

### 📋 Quản lý sự cố mất tài khoản

* Hiển thị danh sách sự cố từ file CSV
* Thêm / Cập nhật / Xóa dữ liệu
* Làm sạch dữ liệu
* Lọc dữ liệu theo mức độ an toàn

### 📊 Trực quan dữ liệu

* Phân bố độ tuổi người dùng
* Thiết bị thường dùng
* Tỷ lệ giới tính
* Mức độ an toàn
* Nguyên nhân mất tài khoản (Pie chart)

---

## ⚠️ LỖI THƯỜNG GẶP

### ❌ Không hiện biểu đồ

```bash
python modules/data_visualization.py
```

### ❌ Lỗi thiếu thư viện

→ Kiểm tra lại các lệnh `pip install`

### ❌ Không load được dữ liệu

→ Kiểm tra file `data/raw_data.csv`

---

## 📬 LIÊN HỆ

* **Email:** [tranghoangbo92@gmail.com](mailto:tranghoangbo92@gmail.com)
* **Github:**
   [https://github.com/bowhitehat/PROJECT_PYTHON_ATTT](https://github.com/bowhitehat/PROJECT_PYTHON_ATTT)

---

```bash
python main.py

