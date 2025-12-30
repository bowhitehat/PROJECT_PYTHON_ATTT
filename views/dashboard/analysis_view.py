import tkinter as tk
from PIL import Image, ImageTk
import os


class AnalysisView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f2f2f2")

        # ===== HEADER =====
        header = tk.Frame(self, bg="#1e2a4a", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        # 🔙 BACK BUTTON (GÓC TRÁI – DỄ THẤY)
        tk.Button(
            header,
            text="⬅ Quay lại",
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            bd=0,
            command=self.go_back
        ).pack(side="left", padx=10)

        # Logo FIT
        logo_path = os.path.join("views", "assets", "logo_fit.png")
        if os.path.exists(logo_path):
            img = Image.open(logo_path).resize((55, 55))
            self.logo = ImageTk.PhotoImage(img)
            tk.Label(header, image=self.logo, bg="#1e2a4a").pack(side="left", padx=10)

        tk.Label(
            header,
            text="TRỰC QUAN DỮ LIỆU",
            fg="white",
            bg="#1e2a4a",
            font=("Arial", 22, "bold")
        ).pack(side="left", padx=10)

        # ===== BODY =====
        body = tk.Frame(self, bg="#f2f2f2")
        body.pack(fill="both", expand=True)

        # ===== MENU LEFT =====
        menu = tk.Frame(body, bg="#1e2a4a", width=240)
        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        tk.Label(
            menu,
            text="DANH MỤC BIỂU ĐỒ",
            fg="white",
            bg="#1e2a4a",
            font=("Arial", 14, "bold")
        ).pack(pady=15)

        self.menu_btn(menu, "Phân bố độ tuổi", lambda: self.show_image("age_distribution.png"))
        self.menu_btn(menu, "Thiết bị sử dụng", lambda: self.show_image("device_usage.png"))
        self.menu_btn(menu, "Tỉ lệ giới tính", lambda: self.show_image("gender_ratio.png"))
        self.menu_btn(menu, "Mức độ an toàn", lambda: self.show_image("security_level.png"))
        self.menu_btn(menu, "Nguyên nhân mất tài khoản", lambda: self.show_image("loss_reason.png"))

        # ===== CONTENT =====
        self.content = tk.Frame(body, bg="white")
        self.content.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        self.image_label = tk.Label(self.content, bg="white")
        self.image_label.pack(expand=True)

        # Hiển thị mặc định
        self.show_image("age_distribution.png")

    # ===== MENU BUTTON =====
    def menu_btn(self, parent, text, command):
        tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 12),
            fg="white",
            bg="#1e2a4a",
            bd=0,
            activebackground="#34495e",
            activeforeground="white",
            height=2
        ).pack(fill="x", padx=15, pady=6)

    # ===== SHOW IMAGE =====
    def show_image(self, filename):
        path = os.path.join("images", filename)
        if not os.path.exists(path):
            self.image_label.config(
                text="❌ Không tìm thấy biểu đồ",
                image="",
                font=("Arial", 14)
            )
            return

        img = Image.open(path).resize((900, 500))
        self.current_img = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.current_img, text="")

    # ===== BACK =====
    def go_back(self):
        self.controller.show_frame("HomeView")
