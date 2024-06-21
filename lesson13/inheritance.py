# Родитель для CompTech и Printer 
# Предок для PersonalComputer и Laptop
class Product:  
    article = '1234567'  
    def __init__(self, price):
        self.price = price * 1.3

# Дочерния для Product
# Родительский для PersonalComputer и Laptop
class CompTech(Product):
    article = '789'
    def __init__(self, ram, ssd, price):
        self.ram = ram
        self.ssd = ssd
        super().__init__(price)

# Дочерний для Comptech
class PersonalComputer(CompTech):
    mobile = False
    
    def can_run_cyberpunk(self):
        if self.ram >= 16 and self.ssd >= 900:
            return True
        else:
            return False

class Laptop(CompTech):
    mobile = True   
    def __init__(self, ram, ssd, screen, price):
        self.screen = screen
        super().__init__(ram, ssd, price)
        
class Printer(Product):
    def __init__(self, color, maker, price):
        self.color = color
        self.maker = maker
        super().__init__(price)


class Cashbox:
    def __init__(self):
        self.value = 0

    def add_money(object_of_class, value):
        object_of_class.value += value

comp_1 = PersonalComputer(8, 500, 700)  
print(comp_1.can_run_cyberpunk()) # False 
comp_2 = PersonalComputer(16, 1000, 1100)  # True

laptop_1 = Laptop(6, 600, 15, 750)
printer_1 = Printer(False, "Samsung", 250)

basket = [comp_1, laptop_1]
for product in basket:
    print(product.price, product.mobile)
