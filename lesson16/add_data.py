# Добавить ряд данных
from openpyxl import load_workbook  # импорт нужной функции


excel_file = load_workbook("product.xlsx")  # обращение к файлу
page = excel_file.active    # обращение к странице

lst = [6, "Mouse", 800, 0.1, "Yes", "iq1000.png"]  # создали строку данных
lst_1 = [7, "Table", 3500, 5, "No", "iq1000.png"]  # создали строку данных

page.append(lst)  # Добавили эти данные на страницу
page.append(lst_1)  # Добавили эти данные на страницу

excel_file.save("product_1.xlsx")




