import tkinter as tk
from ui.dashboard import DashboardApp
from charts.bar_charts import SalesBarChart, InventoryHorizontalBarChart
from charts.pie_charts import ProductPieChart
from charts.line_charts import SalesTrendChart, InventoryAreaChart
from data.data_providers import (
    SalesDataProvider,
    InventoryDataProvider,
    ProductDataProvider,
    SalesYearDataProvider,
    InventoryMonthDataProvider
)

def main():
    root = tk.Tk()
    app = DashboardApp(root)
    
    # Создаем и добавляем все 5 графиков
    app.add_chart(SalesBarChart(SalesDataProvider()), row=0)
    app.add_chart(InventoryHorizontalBarChart(InventoryDataProvider()), row=0)
    app.add_chart(ProductPieChart(ProductDataProvider()), row=0)
    app.add_chart(SalesTrendChart(SalesYearDataProvider()), row=1)
    app.add_chart(InventoryAreaChart(InventoryMonthDataProvider()), row=1)
    
    root.mainloop()

if __name__ == "__main__":
    main()