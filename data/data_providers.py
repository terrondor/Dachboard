from abc import ABC, abstractmethod
from typing import Dict, Any

class DataProvider(ABC):
    @abstractmethod
    def get_data(self) -> Dict[str, Any]:
        pass

class SalesDataProvider(DataProvider):
    def get_data(self) -> Dict[str, int]:
        return {"Product A": 100, "Product B": 200, "Product C": 150}

class InventoryDataProvider(DataProvider):
    def get_data(self) -> Dict[str, int]:
        return {"Product X": 50, "Product Y": 75, "Product Z": 120}

class ProductDataProvider(DataProvider):
    def get_data(self) -> Dict[str, float]:
        return {"Category 1": 35.5, "Category 2": 45.2, "Category 3": 19.3}

class SalesYearDataProvider(DataProvider):
    def get_data(self) -> Dict[int, int]:
        return {2019: 150, 2020: 300, 2021: 450, 2022: 500}

class InventoryMonthDataProvider(DataProvider):
    def get_data(self) -> Dict[str, int]:
        return {"Jan": 100, "Feb": 120, "Mar": 90, "Apr": 110}