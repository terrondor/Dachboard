import tkinter as tk
from config.styles import COLORS

class Sidebar(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=COLORS["primary"], **kwargs)
        self._create_widgets()
        
    def _create_widgets(self):
        label = tk.Label(
            self, 
            text="Dashboard", 
            bg=COLORS["primary"], 
            fg="white", 
            font=("Arial", 14, "bold")
        )
        label.pack(pady=50, padx=20)