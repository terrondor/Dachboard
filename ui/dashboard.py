import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ui.components.sidebar import Sidebar
from config.styles import COLORS

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self._configure_root()
        self._setup_ui()
        
    def _configure_root(self):
        self.root.title("Dashboard")
        self.root.state('zoomed')
        
    def _setup_ui(self):
        self._create_sidebar()
        self._create_main_area()
    
    def _create_sidebar(self):
        self.sidebar = Sidebar(self.root, width=200)
        self.sidebar.pack(side="left", fill="y")
    
    def _create_main_area(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
        
        self.upper_frame = tk.Frame(self.main_frame)
        self.upper_frame.pack(fill="both", expand=True)
        
        self.lower_frame = tk.Frame(self.main_frame)
        self.lower_frame.pack(fill="both", expand=True)
    
    def add_chart(self, chart, row=0):
        frame = self.upper_frame if row == 0 else self.lower_frame
        
        chart.create_chart()
        canvas = FigureCanvasTkAgg(chart.get_figure(), frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left", fill="both", expand=True)