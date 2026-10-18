# -------- Inheritance --------
class Animal:

    def __init__(self, species):
        self.species = species

    def eats(self):
        return f"{self.species} eats its meal ..."


class Dog(Animal):

    def __init__(self):
        super().__init__("Dog")

    def barks(self):
        return f"{self.species} barks ... *woof woof*"


animal1 = Animal("Elephant")
print(animal1.eats())

doggo1 = Dog()
print(doggo1.barks())


# -------- Composition --------
class Engine:
    def start(self):
        return "*Vroom vroom*"


class Car:
    def __init__(self):
        self.engine = Engine()  # Each car has it's own engine (own instance of engine)

    def start_car(self):
        return self.engine.start()  # Delegating the task to the engine


car1 = Car()
print(car1.start_car())
