import tkinter as tk

from views.auth.login_view import LoginView
from views.auth.signup_view import SignupView
from views.dashboard.home_view import HomeView
from views.dashboard.security_view import SecurityView
from views.dashboard.analysis_view import AnalysisView


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Account Security Dashboard - FIT HCMUTE")
        self.geometry("1200x700")
        self.resizable(False, False)

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (LoginView, SignupView, HomeView, SecurityView, AnalysisView):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.user_role = None
        self.show_frame("LoginView")

    def show_frame(self, name):
        self.frames[name].tkraise()

    def set_user_role(self, role):
        self.user_role = role
        if hasattr(self.frames["HomeView"], "set_role"):
            self.frames["HomeView"].set_role(role)


if __name__ == "__main__":
    app = App()
    app.mainloop()
