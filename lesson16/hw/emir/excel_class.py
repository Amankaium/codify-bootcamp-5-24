from openpyxl import load_workbook


class ExcelClass:
    def __init__(self, file_name):
        self.file_name = file_name
        self.excel_file = load_workbook("product.xlsx")  # обращение к файлу
        self.page = self.excel_file.active

    # создание новой строки данных
    def create_row(self, new_lst):
        self.page.append(new_lst)

    # чтение всей строки + его наименование
    def read_row(self, row_number):
        row = self.page[str(row_number)]
        row_name = self.page["1"]
        name_values = [cell.value for cell in row_name]
        row_values = [cell.value for cell in row]
        data = ""
        for name, value in zip(name_values, row_values):
            data += f"{name}: {value}\n"
        return data

    def read_row_photo(self, row_number):
        return self.page[f"F{row_number}"].value

    # чтение ячейки
    def read_cell(self, coords):
        cell_value = self.page[coords].value
        print(f"в ячейке {coords}: {cell_value}")

    # изменение ячейки
    def update_cell(self, coords, new_value):
        self.page[coords] = new_value

    # удаление ячейки
    def delete_cell(self, coords):
        self.page[coords] = None

    # получение списка цен
    def get_pricelist(self):
        data = ""
        for row in self.page["B2:C6"]:
            product_name = row[0].value
            product_price = row[1].value
            data += f"{product_name} - {product_price} som\n"
        return data


file = ExcelClass("product.xlsx")

# file.read_cell("A1")
file.get_pricelist()
