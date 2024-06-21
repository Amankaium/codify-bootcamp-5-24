class Product():
    def __init__(self, name, price, photo):
        self.name = name
        self.price = price
        self.photo = photo


my_cup = Product("Кружка", 250, "my_cup.jpg")
my_cat = Product("Плюшевый кот", 340, "cat.jpg")
my_laptop = Product("Ноутбук", 27000, "my_laptop.jpg")

products_list = [my_cup, my_cat, my_laptop]
