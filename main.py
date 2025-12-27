import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

from controllers.auth_controller import handle_login, handle_signup
from controllers.analysis_controller import clean_data, analyze_data, visualize_data

# ================= AUTH =================
def login():
    username = entry_user.get()
    password = entry_pass.get()

    role = handle_login(username, password)
    if role:
        messagebox.showinfo("Success", f"Login successful ({role})")
        open_dashboard(role)
    else:
        messagebox.showerror("Error", "Invalid username or password")

def register():
    username = entry_user.get()
    password = entry_pass.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter username and password")
        return

    if handle_signup(username, password):
        messagebox.showinfo("Success", "Register successful! You can login now.")
    else:
        messagebox.showerror("Error", "Username already exists")

# ================= SHOW CHARTS =================
def show_charts():
    visualize_data()  # tạo ảnh trước

    chart_win = tk.Toplevel(root)
    chart_win.title("Charts")
    chart_win.geometry("900x700")
    chart_win.configure(bg="#f5f6fa")

    tk.Label(
        chart_win,
        text="Account Security Charts",
        font=("Segoe UI", 16, "bold"),
        bg="#f5f6fa"
    ).pack(pady=10)

    canvas = tk.Canvas(chart_win, bg="#f5f6fa")
    scrollbar = tk.Scrollbar(chart_win, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="#f5f6fa")

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    images = ["age_chart.png", "privacy_chart.png", "device_chart.png"]

    for img_name in images:
        img_path = os.path.join("images", img_name)
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((700, 450))
            photo = ImageTk.PhotoImage(img)

            lbl = tk.Label(scroll_frame, image=photo, bg="#f5f6fa")
            lbl.image = photo
            lbl.pack(pady=15)

# ================= DASHBOARD =================
def open_dashboard(role):
    dash = tk.Toplevel(root)
    dash.title("Dashboard")
    dash.geometry("520x420")
    dash.configure(bg="#f5f6fa")

    tk.Label(
        dash,
        text="Account Security Dashboard",
        font=("Segoe UI", 16, "bold"),
        bg="#f5f6fa"
    ).pack(pady=20)

    tk.Label(
        dash,
        text=f"Role: {role}",
        font=("Segoe UI", 11),
        bg="#f5f6fa"
    ).pack(pady=5)

    btn_frame = tk.Frame(dash, bg="#f5f6fa")
    btn_frame.pack(pady=30)

    if role == "admin":
        tk.Button(btn_frame, text="Clean Data", width=22, height=2,
                  bg="#4CAF50", fg="white", command=clean_data).pack(pady=6)

        tk.Button(btn_frame, text="Analyze Data", width=22, height=2,
                  bg="#2196F3", fg="white", command=analyze_data).pack(pady=6)

        tk.Button(btn_frame, text="View Charts", width=22, height=2,
                  bg="#9C27B0", fg="white", command=show_charts).pack(pady=6)
    else:
        tk.Button(btn_frame, text="View Charts", width=22, height=2,
                  bg="#2196F3", fg="white", command=show_charts).pack(pady=6)

# ================= MAIN WINDOW =================
root = tk.Tk()
root.title("Account Security System")
root.geometry("440x380")
root.configure(bg="#ecf0f1")
root.resizable(False, False)

card = tk.Frame(root, bg="white", bd=2, relief="groove")
card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=300)

tk.Label(
    card,
    text="LOGIN / REGISTER",
    font=("Segoe UI", 14, "bold"),
    bg="white"
).pack(pady=15)

tk.Label(card, text="Username", bg="white", anchor="w").pack(fill="x", padx=25)
entry_user = tk.Entry(card, font=("Segoe UI", 11))
entry_user.pack(padx=25, pady=5, fill="x")

tk.Label(card, text="Password", bg="white", anchor="w").pack(fill="x", padx=25)
entry_pass = tk.Entry(card, show="*", font=("Segoe UI", 11))
entry_pass.pack(padx=25, pady=5, fill="x")

tk.Button(
    card,
    text="Login",
    font=("Segoe UI", 11),
    bg="#2ecc71",
    fg="white",
    command=login
).pack(pady=10, padx=25, fill="x")

tk.Button(
    card,
    text="Register",
    font=("Segoe UI", 11),
    bg="#3498db",
    fg="white",
    command=register
).pack(pady=5, padx=25, fill="x")

root.mainloop()
