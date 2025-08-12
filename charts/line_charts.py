from charts.base_chart import Chart

class SalesTrendChart(Chart):
    def create_chart(self):
        data = self.data_provider.get_data()
        self.ax.plot(list(data.keys()), list(data.values()))
        self.ax.set_title("Sales by Year")
        self.ax.set_xlabel("Year")
        self.ax.set_ylabel("Sales")

class InventoryAreaChart(Chart):
    def create_chart(self):
        data = self.data_provider.get_data()
        self.ax.fill_between(data.keys(), data.values())
        self.ax.set_title("Inventory by Month")
        self.ax.set_xlabel("Month")
        self.ax.set_ylabel("Inventory")