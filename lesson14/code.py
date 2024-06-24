# pip install openpyxl
from openpyxl import load_workbook


excel_file = load_workbook("marks.xlsx")  # открываем файл
page = excel_file["Лист1"]  # обращаемся к листу в excel
# print(page["D2"].value)  # обращение к ячейке (к свойству value)

# for row in page:
#     for cell in row:
#         print(cell.value)

page["E1"] = "Средняя"

for row in page["B2:D5"]:
    # [77, 88, 89]
    sm = 0
    qty = 0
    for cell in row:
        sm += cell.value
        qty += 1
        # print(cell.column_letter, cell.row)
    row_value = cell.row  # 2 # есть ещё и column
    page[f"E{row_value}"] = sm / qty
    

# Добавить 1 ряд: Безназар с оценками, 
# и переделать программу под 4 студентов