import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
from PIL import Image, ImageTk

DATA_PATH = "data/raw_data.csv"

COLUMNS = [
    "account_id", "timestamp", "age_range", "gender",
    "device", "loss_times", "loss_reason", "recovered", "security_level"
]


class SecurityView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.df = pd.DataFrame()

        self.build_ui()
        self.load_data()

    # ================= UI =================
    def build_ui(self):
        # ===== HEADER =====
        header = tk.Frame(self, bg="#1e2a4a", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        logo_path = os.path.join("views", "assets", "logo_fit.png")
        if os.path.exists(logo_path):
            img = Image.open(logo_path).resize((50, 50))
            self.logo = ImageTk.PhotoImage(img)
            tk.Label(header, image=self.logo, bg="#1e2a4a").pack(side="left", padx=15)

        tk.Label(
            header, text="QUẢN LÝ SỰ CỐ MẤT TÀI KHOẢN",
            fg="white", bg="#1e2a4a",
            font=("Arial", 20, "bold")
        ).pack(side="left")

        # ===== FILTER =====
        filter_frame = tk.Frame(self)
        filter_frame.pack(pady=5)

        tk.Label(filter_frame, text="Lọc theo mức độ an toàn:").pack(side="left", padx=5)
        self.filter_var = tk.StringVar(value="All")

        ttk.Combobox(
            filter_frame,
            textvariable=self.filter_var,
            values=["All", "Low", "Medium", "High"],
            width=10
        ).pack(side="left")

        tk.Button(filter_frame, text="Lọc", command=self.apply_filter).pack(side="left", padx=5)

        # ===== TABLE =====
        table_frame = tk.Frame(self)
        table_frame.pack(fill="both", expand=True, padx=10)

        self.tree = ttk.Treeview(table_frame, columns=COLUMNS, show="headings")
        for col in COLUMNS:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # ===== BUTTONS =====
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Thêm", command=self.add_row).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Cập nhật", command=self.update_row).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Xóa dòng", command=self.delete_row).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Làm sạch dữ liệu", command=self.clean_data).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Quay lại", command=lambda: self.controller.show_frame("HomeView")).pack(side="left", padx=5)

    # ================= DATA =================
    def load_data(self):
        if not os.path.exists(DATA_PATH):
            return

        self.df = pd.read_csv(DATA_PATH, sep=";")
        self.refresh_table(self.df)

    def refresh_table(self, df):
        self.tree.delete(*self.tree.get_children())
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def apply_filter(self):
        level = self.filter_var.get()
        if level == "All":
            self.refresh_table(self.df)
        else:
            self.refresh_table(self.df[self.df["security_level"].str.lower() == level.lower()])

    # ================= CRUD =================
    def add_row(self):
        self.open_form("Thêm sự cố")

    def update_row(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Chọn dòng", "Vui lòng chọn dòng để cập nhật")
            return

        values = self.tree.item(selected[0])["values"]
        self.open_form("Cập nhật sự cố", values)

    def delete_row(self):
        selected = self.tree.selection()
        if not selected:
            return

        if not messagebox.askyesno("Xác nhận", "Xóa dòng đã chọn?"):
            return

        account_id = self.tree.item(selected[0])["values"][0]
        self.df = self.df[self.df["account_id"] != account_id]
        self.df.to_csv(DATA_PATH, sep=";", index=False)
        self.refresh_table(self.df)

    def clean_data(self):
        self.df = self.df.dropna()
        for col in self.df.columns:
            self.df[col] = self.df[col].astype(str).str.strip().str.lower()

        self.df.to_csv(DATA_PATH, sep=";", index=False)
        self.refresh_table(self.df)
        messagebox.showinfo("OK", "Đã làm sạch dữ liệu")

    # ================= FORM =================
    def open_form(self, title, values=None):
        win = tk.Toplevel(self)
        win.title(title)

        entries = {}
        for i, col in enumerate(COLUMNS):
            tk.Label(win, text=col).grid(row=i, column=0, padx=5, pady=3)
            ent = tk.Entry(win, width=30)
            ent.grid(row=i, column=1, padx=5, pady=3)
            if values:
                ent.insert(0, values[i])
            entries[col] = ent

        def save():
            data = {c: entries[c].get() for c in COLUMNS}
            if values:
                self.df.loc[self.df["account_id"] == values[0]] = data
            else:
                self.df = pd.concat([self.df, pd.DataFrame([data])])

            self.df.to_csv(DATA_PATH, sep=";", index=False)
            self.refresh_table(self.df)
            win.destroy()

        tk.Button(win, text="Lưu", command=save).grid(row=len(COLUMNS), column=0, columnspan=2, pady=10)
