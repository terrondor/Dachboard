from charts.base_chart import Chart

class SalesBarChart(Chart):
    def create_chart(self):
        data = self.data_provider.get_data()
        self.ax.bar(data.keys(), data.values())
        self.ax.set_title("Sales by Product")
        self.ax.set_xlabel("Product")
        self.ax.set_ylabel("Sales")

class InventoryHorizontalBarChart(Chart):
    def create_chart(self):
        data = self.data_provider.get_data()
        self.ax.barh(list(data.keys()), data.values())
        self.ax.set_title("Inventory by Product")
        self.ax.set_xlabel("Inventory")
        self.ax.set_ylabel("Product")