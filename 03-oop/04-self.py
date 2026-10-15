class Meal:
    quantity = 2

    def prepare(self):
        return f"Preparing {self.quantity} meals ..."


dish1 = Meal()
print(dish1.prepare())

# or if we want to access the method using the class itself
print(Meal.prepare(dish1))
# we need to still pass an object whose method we would be using
# Works like call/bind/apply in JS ig ?
