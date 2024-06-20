a = "hi"
# print(type(a))

class Child:
    age = 10
    can_speak = True
    name = "Bob"

    def run(self):
        print("running...")

bob = Child() # объект класса Child
print(type(bob))
print(bob.age)  # свойство объекта
bob.run()
