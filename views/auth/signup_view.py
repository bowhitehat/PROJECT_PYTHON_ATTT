import tkinter as tk
from tkinter import messagebox
from controllers.auth_controller import handle_signup


class SignupView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="white")

        container = tk.Frame(self, bg="white")
        container.pack(expand=True)

        tk.Label(
            container,
            text="ĐĂNG KÍ TÀI KHOẢN",
            font=("Arial", 22, "bold"),
            bg="white"
        ).pack(pady=20)

        # Username
        tk.Label(container, text="Username", bg="white").pack(anchor="w")
        self.username = tk.Entry(container, font=("Arial", 14), width=30)
        self.username.pack(pady=5)

        # Password
        tk.Label(container, text="Password", bg="white").pack(anchor="w")
        self.password = tk.Entry(container, show="*", font=("Arial", 14), width=30)
        self.password.pack(pady=5)

        # Confirm password
        tk.Label(container, text="Xác nhận mật khẩu", bg="white").pack(anchor="w")
        self.confirm_password = tk.Entry(container, show="*", font=("Arial", 14), width=30)
        self.confirm_password.pack(pady=5)

        tk.Button(
            container,
            text="Đăng kí",
            font=("Arial", 14),
            bg="#27ae60",
            fg="white",
            command=self.signup
        ).pack(pady=20, ipadx=20, ipady=5)

        tk.Button(
            container,
            text="⬅ Quay lại đăng nhập",
            bg="white",
            fg="blue",
            bd=0,
            command=lambda: controller.show_frame("LoginView")
        ).pack()

    def signup(self):
        username = self.username.get()
        password = self.password.get()
        confirm = self.confirm_password.get()

        if not username or not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
            return

        if password != confirm:
            messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp")
            return

        success = handle_signup(username, password)
        if success:
            messagebox.showinfo(
                "Đăng kí thành công",
                "Tài khoản đã được tạo!\nVui lòng đăng nhập."
            )
            self.controller.show_frame("LoginView")
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại")
