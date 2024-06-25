# ДЗ: 
# Используя библиотеку openpyxl, решить
# 1. Из этого файла получить среднюю по уроку (по колонне). Сделать задание не используя классы
# 2. То же самое задание, используя классы
# 3. Получить общее среднее и записать в ячейку Е5


from openpyxl import load_workbook


excel_file = load_workbook("marks.xlsx")  # открываем файл
page = excel_file["Лист1"]  # обращаемся к листу в excel

page["E1"] = "Средняя"

for row in page["B2:D4"]:
    # [77, 88, 89]
    sm = 0
    qty = 0
    for cell in row:
        sm += cell.value
        qty += 1
        # print(cell.column_letter, cell.row)
    row_value = cell.row  # 2 # есть ещё и column
    page[f"E{row_value}"] = sm / qty

page["A5"] = "Средняя"
result = {}
for row in page["B2:D4"]:
    for cell in row:  # C3 # 54
        letter = cell.column_letter  # "C"  <------
        if letter not in result:  # "C" not in result # False
            result[letter] = {"sum": 0, "qty": 0} # {"D": {"sum": 0, "qty": 0}}
        
        # {
            # "B": {"sum": 275, "qty": 3}, 
            # "C": {"sum": 220, "qty": 3}, 
            # "D": {"sum": 230, "qty": 3}
        # }
        number = cell.value  # 54
        result[letter]["sum"] += number
        result[letter]["qty"] += 1
         
# result = {
    # "B": {"sum": 275, "qty": 3}, 
    # "C": {"sum": 220, "qty": 3}, 
    # "D": {"sum": 230, "qty": 3}
# }
# Получить и записали среднюю арифметическую каждой буквы           
for l in result:
    m = result[l]["sum"] / result[l]["qty"]
    page[f"{l}5"] = m



excel_file.save("res.xlsx")
