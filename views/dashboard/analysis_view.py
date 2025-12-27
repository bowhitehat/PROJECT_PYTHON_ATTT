import tkinter as tk
from PIL import Image, ImageTk
import os


class AnalysisView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="TRỰC QUAN DỮ LIỆU", font=("Arial", 22, "bold")).pack(pady=10)

        img_path = os.path.join("images", "device_chart.png")
        if os.path.exists(img_path):
            img = Image.open(img_path).resize((800, 400))
            self.img = ImageTk.PhotoImage(img)
            tk.Label(self, image=self.img).pack()

        tk.Button(self, text="Quay lại", command=lambda: controller.show_frame("HomeView")).pack(pady=10)
