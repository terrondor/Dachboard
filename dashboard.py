import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data

# Установка цветовой схемы для графиков
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#44944A", "#A8E4A0", "#47A76A", "#004524", "#30BA8F"])

# График 1: Столбчатая диаграмма данных о продажах
fig1, ax1 = plt.subplots()
ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Sales by Product")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")
# plt.show()

# График 2: Горизонтальная столбчатая диаграмма данных о запасах
fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), inventory_data.values())
ax2.set_title("Inventory by Product")
ax2.set_xlabel("Inventory")
ax2.set_ylabel("Product")
# plt.show()

# График 3: Круговая диаграмма данных о продуктах
fig3, ax3 = plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
ax3.set_title("Product \nBreakdown")
# plt.show()

# График 4: Линейный график продаж по годам
fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title("Sales by Year")
ax4.set_xlabel("Year")
ax4.set_ylabel("Sales")
# plt.show()

# График 5: Диаграмма с областями запасов по месяцам
fig5, ax5 = plt.subplots()
ax5.fill_between(inventory_month_data.keys(),
                 inventory_month_data.values())
ax5.set_title("Inventory by Month")
ax5.set_xlabel("Month")
ax5.set_ylabel("Inventory")
# plt.show()

# Создание окна и добавление графиков
root = tk.Tk()
root.title("Dashboard")
root.state('zoomed')

# Боковая панель
side_frame = tk.Frame(root, bg="#2E8B57")
side_frame.pack(side="left", fill="y")

# Заголовок на боковой панели
label = tk.Label(side_frame, text="Dashboard", bg="#2E8B57", fg="#FFF", font=25)
label.pack(pady=50, padx=20)

# Основная область для графиков
charts_frame = tk.Frame(root)
charts_frame.pack()

# Верхняя часть с тремя графиками
upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)

# Добавление графиков 1-3 в верхнюю часть
canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

# Нижняя часть с двумя графиками
lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

# Добавление графиков 4-5 в нижнюю часть
canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
canvas5.draw()
canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)

# Запуск основного цикла приложения
root.mainloop()