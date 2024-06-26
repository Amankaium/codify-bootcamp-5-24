# CRUD
# Create, Read, Update, Delete

from openpyxl import load_workbook


class ExcelClass:
    def __init__(self, file_name):
        self.file_name = file_name
        self.excel_file = load_workbook("product.xlsx")  # обращение к файлу
        self.page = self.excel_file.active
     
    # создание новой строки данных
    def create_row(self, new_lst):
        self.page.append(new_lst)
    
    # чтение всей строки
    def read_row(self, row_number):
        row = self.page[str(row_number)]
        data = ""
        for cell in row:
            data += f"{cell.value}\n"
        return data
    
    def read_row_photo(self, row_number):
        return self.page[f"F{row_number}"].value
    
    # изменение ячейки
    def update_cell(self, coords, new_value):
        self.page[coords] = new_value
    
    # удаление ячейки
    def delete_cell(self, coords):
        self.page[coords] = None



