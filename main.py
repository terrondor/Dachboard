import tkinter as tk
from ui.dashboard import DashboardApp
from charts.bar_charts import SalesBarChart, InventoryHorizontalBarChart
from data.data_providers import SalesDataProvider, InventoryDataProvider

def main():
    root = tk.Tk()
    app = DashboardApp(root)
    
    # Добавляем графики
    sales_chart = SalesBarChart(SalesDataProvider())
    inventory_chart = InventoryHorizontalBarChart(InventoryDataProvider())
    
    app.add_chart(sales_chart, row=0)
    app.add_chart(inventory_chart, row=1)
    
    root.mainloop()

if __name__ == "__main__":
    main()