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

    def read_cell(self, row_number):
        row = self.page[str(row_number)]
        row_1 = self.page[str(1)]
        data = ""
        for cell in row:
            data += f"{cell.value}\n"
        data_1 = ""
        for cell in row_1:
            data_1 += f"{cell.value}\n"
        data_1_parts = data_1.split('\n')
        data_parts = data.split('\n')
        result_lines = []
        for part1, part2 in zip(data_1_parts, data_parts):
            result_lines.append(f"{part1}: {part2}")
        a = '\n'.join(result_lines)
        return a

    def price_lst(self):
        lst_price = []
        for row in self.page["B2:C6"]:
            row_lst = ""
            for cell in row:
                row_lst += f"{cell.value}\t"
            lst_price.append(row_lst)
        b = '\n'.join(lst_price)
        return b

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


