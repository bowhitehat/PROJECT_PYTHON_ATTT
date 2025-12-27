import tkinter as tk
from PIL import Image, ImageTk
import os

class HomeView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f2f2f2")
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
            text="TRANG CHỦ",
            fg="white",
            bg="#1e2a4a",
            font=("Arial", 22, "bold")
        ).pack(side="left")

        # ===== BODY =====
        body = tk.Frame(self, bg="#f2f2f2")
        body.pack(fill="both", expand=True)

        # ===== MENU =====
        menu = tk.Frame(body, bg="#1e2a4a", width=220)
        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        tk.Label(menu, text="Menu", fg="white", bg="#1e2a4a",
                 font=("Arial", 14, "bold")).pack(pady=15)

        self.menu_btn(menu, "Quản lý sự cố", lambda: controller.show_frame("SecurityView"))
        self.menu_btn(menu, "Trực quan", lambda: controller.show_frame("AnalysisView"))
        self.menu_btn(menu, "Đăng xuất", lambda: controller.show_frame("LoginView"))
        self.menu_btn(menu, "Thoát", controller.destroy)

        # ===== CONTENT =====
        self.content = tk.Frame(body, bg="white")
        self.content.pack(side="left", fill="both", expand=True)

        self.show_home()

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
            height=2
        ).pack(fill="x", padx=10, pady=5)

    def show_home(self):
        for w in self.content.winfo_children():
            w.destroy()

        bg_path = os.path.join("views", "assets", "bg_home.png")
        if os.path.exists(bg_path):
            img = Image.open(bg_path).resize((900, 550))
            self.bg = ImageTk.PhotoImage(img)
            tk.Label(self.content, image=self.bg).pack()
