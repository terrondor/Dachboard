import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ui.components.sidebar import Sidebar
from config.styles import COLORS
import matplotlib.pyplot as plt

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self._configure_root()
        self._setup_ui()
        self._configure_matplotlib()
        
    def _configure_root(self):
        self.root.title("Dashboard")
        self.root.state('zoomed')
        
    def _configure_matplotlib(self):
        plt.rcParams["axes.prop_cycle"] = plt.cycler(
            color=COLORS["chart_colors"])
        
    def _setup_ui(self):
        self._create_sidebar()
        self._create_main_area()
    
    def _create_sidebar(self):
        self.sidebar = Sidebar(self.root, width=200)
        self.sidebar.pack(side="left", fill="y")
    
    def _create_main_area(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
        
        # Верхний ряд (3 графика)
        self.upper_frame = tk.Frame(self.main_frame)
        self.upper_frame.pack(fill="both", expand=True)
        
        # Нижний ряд (2 графика)
        self.lower_frame = tk.Frame(self.main_frame)
        self.lower_frame.pack(fill="both", expand=True)
    
    def add_chart(self, chart, row=0):
        frame = self.upper_frame if row == 0 else self.lower_frame
        
        chart.create_chart()
        canvas = FigureCanvasTkAgg(chart.get_figure(), frame)
        canvas.draw()
        canvas.get_tk_widget().pack(
            side="left", 
            fill="both", 
            expand=True, 
            padx=10, 
            pady=10
        )