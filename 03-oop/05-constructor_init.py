class Drink:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type}."


drink1 = Drink("Masala Chai", 150)
print(drink1.summary())

drink2 = Drink("Ginger Ale", 250)
print(drink2.summary())
