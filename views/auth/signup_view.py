import tkinter as tk
from controllers.auth_controller import handle_signup

class SignupView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="white")

        tk.Label(self, text="ĐĂNG KÝ", font=("Arial", 22, "bold"), bg="white").pack(pady=30)

        self.username = tk.Entry(self, font=("Arial", 14))
        self.password = tk.Entry(self, font=("Arial", 14), show="*")

        tk.Label(self, text="Username", bg="white").pack()
        self.username.pack()

        tk.Label(self, text="Password", bg="white").pack()
        self.password.pack()

        tk.Button(self, text="Tạo tài khoản", command=self.signup).pack(pady=15)

        tk.Button(
            self, text="← Quay lại đăng nhập",
            bg="white", fg="blue", bd=0,
            command=lambda: controller.show_frame("LoginView")
        ).pack()

    def signup(self):
        handle_signup(self.username.get(), self.password.get())
