class Meal:
    temperature = "hot"
    spice_level = "high"


dish1 = Meal()

dish1.temperature = "Mild"
dish1.quantity = "2"


print(f"Before the change temperature is {dish1.temperature}")
print(f"Before the change quantity is {dish1.quantity}")
print(f"In the class the temperature is {Meal.temperature}")

del dish1.temperature
print(
    f"After the change temperature is {dish1.temperature}"
)  # falls-back to the class attr

del dish1.quantity
print(f"Deleting quantity {dish1.quantity}")  # no class attr to fall back to -> error
