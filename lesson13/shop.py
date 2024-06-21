class Computer:
    def __init__(self, ram, ssd, price):
        self.ram = ram
        self.ssd = ssd
        self.price = price

class Laptop:
    def __init__(self, ram, ssd, screen, price):
        self.ram = ram
        self.ssd = ssd
        self.screen = screen
        self.price = price

class Printer:
    def __init__(self, color, maker, price):
        self.color = color
        self.maker = maker
        self.price = price

class Cashbox:
    def __init__(self):
        self.value = 0
    
    def add_money(object_of_class, value):
        object_of_class.value += value

# создали кассу
cashbox_2106 = Cashbox()
print(cashbox_2106.value)  # 0
# cashbox_2106.add_money(1000)
# print(cashbox_2106.value)  # 1000

# создаём товары
comp_hp = Computer(8, 500, 700)
printer_1 = Printer(True, 'Sony', 500)

# товары продали
cashbox_2106.add_money(printer_1.price)
cashbox_2106.add_money(comp_hp.price)
print(cashbox_2106.value)  # 1200


