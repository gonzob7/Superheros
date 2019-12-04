class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating")

    def drink(self):
        print(self.name + " is drinking")

class Frog(Animal):
    def jump(self):
        print(self.name + " is jumping")


a1 = Animal("Tiger")
a1.eat()
a1.drink()

frog1 = Frog("Froggy")
frog1.eat()
frog1.drink()
frog1.jump()
