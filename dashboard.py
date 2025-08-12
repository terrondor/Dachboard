import matplotlib.pyplot as plt
from data import (
    sales_data,
    inventory_data,
    product_data,
    sales_year_data,
    inventory_month_data,
)


plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"]
)

fig1, ax1 = plt.subplots()
ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Продажи продукта")
ax1.set_xlabel("Продукт")
ax1.set_ylabel("Продажи")
"""plt.show()"""


fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), inventory_data.values())
ax2.set_title("Продукты в инвентаре")
ax2.set_xlabel("Инвентарь")
ax2.set_ylabel("Продукты")
"""plt.show()"""

fig3, ax3 = plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
ax3.set_title('Проданные продукты')
"""plt.show()"""


fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title('Продажи за год')
ax4.set_xlabel('Год')
ax4.set_ylabel('Продажи')
"""plt.show()"""

fig5, ax5 = plt.subplots()
ax5.fill_between(inventory_month_data.keys(),
                 inventory_month_data.values())
ax5.set_title('Инвентарь за месяц')
ax5.set_xlabel('Месяц')
ax5.set_ylabel('Инвентарь')
"""plt.show()"""
