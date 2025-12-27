import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
from PIL import Image, ImageTk


DATA_PATH = "data/raw_data.csv"


class SecurityView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # ===== HEADER =====
        header = tk.Frame(self, bg="#1e2a4a", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        logo_path = os.path.join("views", "assets", "logo_fit.png")
        if os.path.exists(logo_path):
            img = Image.open(logo_path).resize((60, 60))
            self.logo = ImageTk.PhotoImage(img)
            tk.Label(header, image=self.logo, bg="#1e2a4a").pack(side="left", padx=20)

        tk.Label(
            header,
            text="QUẢN LÝ SỰ CỐ MẤT TÀI KHOẢN",
            fg="white",
            bg="#1e2a4a",
            font=("Arial", 22, "bold")
        ).pack(side="left")

        # ===== FILTER =====
        filter_frame = tk.Frame(self)
        filter_frame.pack(pady=10)

        tk.Label(filter_frame, text="Lọc theo mức độ an toàn:").pack(side="left")
        self.level_var = tk.StringVar(value="All")
        self.level_box = ttk.Combobox(
            filter_frame,
            textvariable=self.level_var,
            values=["All", "Low", "Medium", "High"],
            width=10
        )
        self.level_box.pack(side="left", padx=5)

        tk.Button(filter_frame, text="Lọc", command=self.load_data).pack(side="left")

        # ===== TABLE =====
        self.tree = ttk.Treeview(self, show="headings")
        self.tree.pack(fill="both", expand=True, padx=10)

        self.columns = [
            "account_id", "timestamp", "age_range", "gender", "device",
            "loss_times", "loss_reason", "recovered", "security_level"
        ]
        self.tree["columns"] = self.columns

        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        # ===== BUTTONS =====
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Thêm", command=self.add_row).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Cập nhật", command=self.update_row).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Xóa dòng", command=self.delete_row).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Làm sạch dữ liệu", command=self.clean_data).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Quay lại", command=lambda: controller.show_frame("HomeView")).pack(side="left", padx=5)

        self.load_data()

    # ===== DATA =====
    def load_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        df = pd.read_csv(DATA_PATH, sep=";")

        level = self.level_var.get()
        if level != "All":
            df = df[df["security_level"].str.lower() == level.lower()]

        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def add_row(self):
        messagebox.showinfo("Thông báo", "Chức năng thêm: sẽ nhập form sau")

    def update_row(self):
        messagebox.showinfo("Thông báo", "Chức năng cập nhật đang xử lý")

    def delete_row(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Lỗi", "Chọn dòng cần xóa")
            return

        item = self.tree.item(selected[0])
        account_id = item["values"][0]

        df = pd.read_csv(DATA_PATH, sep=";")
        df = df[df["account_id"] != account_id]
        df.to_csv(DATA_PATH, sep=";", index=False)

        self.load_data()

    def clean_data(self):
        df = pd.read_csv(DATA_PATH, sep=";")
        df.dropna(inplace=True)
        df.to_csv(DATA_PATH, sep=";", index=False)
        self.load_data()
