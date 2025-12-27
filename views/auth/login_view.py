import tkinter as tk
from PIL import Image, ImageTk
import os
from controllers.auth_controller import handle_login
from tkinter import messagebox


class LoginView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="white")

        # ===== LOGOS =====
        logo_frame = tk.Frame(self, bg="white")
        logo_frame.pack(pady=10)

        ute_path = os.path.join("views", "assets", "logo_ute.png")
        fit_path = os.path.join("views", "assets", "logo_fit.png")

        if os.path.exists(ute_path):
            ute_img = Image.open(ute_path).resize((60, 60))
            self.logo_ute = ImageTk.PhotoImage(ute_img)
            tk.Label(logo_frame, image=self.logo_ute, bg="white").pack(side="left", padx=10)

        if os.path.exists(fit_path):
            fit_img = Image.open(fit_path).resize((60, 60))
            self.logo_fit = ImageTk.PhotoImage(fit_img)
            tk.Label(logo_frame, image=self.logo_fit, bg="white").pack(side="left", padx=10)

        # ===== MAIN BODY =====
        body = tk.Frame(self, bg="white")
        body.pack(fill="both", expand=True)

        # LEFT IMAGE
        img_path = os.path.join("views", "assets", "bg_home.png")
        if os.path.exists(img_path):
            img = Image.open(img_path).resize((650, 650))
            self.bg_img = ImageTk.PhotoImage(img)
            tk.Label(body, image=self.bg_img, bg="white").pack(side="left")

        # RIGHT FORM
        right = tk.Frame(body, bg="white")
        right.pack(side="right", expand=True, fill="both", padx=40)

        tk.Label(
            right,
            text="ĐĂNG NHẬP",
            font=("Arial", 22, "bold"),
            bg="white"
        ).pack(pady=30)

        tk.Label(right, text="Username", bg="white").pack(anchor="w")
        self.username = tk.Entry(right, font=("Arial", 14), width=25)
        self.username.pack(pady=5)

        tk.Label(right, text="Password", bg="white").pack(anchor="w")
        self.password = tk.Entry(right, font=("Arial", 14), show="*", width=25)
        self.password.pack(pady=5)

        tk.Button(
            right,
            text="Sign In",
            font=("Arial", 14),
            bg="#1f2a44",
            fg="white",
            command=self.login
        ).pack(pady=20, ipadx=40, ipady=5)

        tk.Button(
            right,
            text="Bạn chưa có tài khoản? Đăng ký",
            bg="white",
            fg="blue",
            bd=0,
            command=lambda: controller.show_frame("SignupView")
        ).pack()

    def login(self):
        role = handle_login(self.username.get(), self.password.get())
        if role:
            self.controller.set_user_role(role)
            self.controller.show_frame("HomeView")
        else:
            messagebox.showerror("Lỗi", "Sai username hoặc password")
