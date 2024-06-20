class Human:
    hands = 2
    legs = 2
    can_speak = True

    def __init__(self, personal_name, age):
        self.name = personal_name
        self.age = age
    
    def grow(self):
        self.age += 1


daniel = Human("Daniel", 21)
# print(daniel.can_speak)
# print(daniel.name)
# print(daniel.age)  # 21
daniel.grow()  # стал старше
# print(daniel.age)  # 22
 

emir = Human("Emir", 15)
# print(emir.age)  # 15
daniel.grow()
# print(emir.age)  # 15
