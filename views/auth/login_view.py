import tkinter as tk
from PIL import Image, ImageTk
import os
from controllers.auth_controller import handle_login

class LoginView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="white")

        # LEFT IMAGE
        img_path = os.path.join("views", "assets", "bg_home.png")
        img = Image.open(img_path).resize((650, 650))
        self.bg_img = ImageTk.PhotoImage(img)

        tk.Label(self, image=self.bg_img).pack(side="left")

        # RIGHT FORM
        right = tk.Frame(self, bg="white")
        right.pack(side="right", expand=True, fill="both", padx=40)

        tk.Label(right, text="ĐĂNG NHẬP", font=("Arial", 22, "bold"), bg="white").pack(pady=30)

        self.username = tk.Entry(right, font=("Arial", 14), width=25)
        self.password = tk.Entry(right, font=("Arial", 14), show="*", width=25)

        tk.Label(right, text="Username", bg="white").pack(anchor="w")
        self.username.pack(pady=5)

        tk.Label(right, text="Password", bg="white").pack(anchor="w")
        self.password.pack(pady=5)

        tk.Button(
            right, text="Sign In", font=("Arial", 14),
            bg="#1f2a44", fg="white",
            command=self.login
        ).pack(pady=20, ipadx=40, ipady=5)

        tk.Button(
            right, text="Bạn chưa có tài khoản? Đăng ký",
            bg="white", fg="blue", bd=0,
            command=lambda: controller.show_frame("SignupView")
        ).pack()

    def login(self):
        role = handle_login(self.username.get(), self.password.get())
        if role:
            self.controller.set_user_role(role)
            self.controller.show_frame("HomeView")
