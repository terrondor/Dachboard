from charts.base_chart import Chart

class ProductPieChart(Chart):
    def create_chart(self):
        data = self.data_provider.get_data()
        self.ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
        self.ax.set_title("Product Breakdown")