from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from data.data_providers import DataProvider

class Chart(ABC):
    def __init__(self, data_provider: DataProvider):
        self.data_provider = data_provider
        self.fig, self.ax = plt.subplots()
        
    @abstractmethod
    def create_chart(self):
        pass
        
    def get_figure(self):
        return self.fig