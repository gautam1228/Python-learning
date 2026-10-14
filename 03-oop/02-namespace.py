class Meal:
    origin = "India"


print(Meal.origin)

Meal.is_hot = True
print(Meal.is_hot)

# Creating an instance of the Meal class
plate1 = Meal()
print(f"Plate {plate1.origin}")
print(f"Plate {plate1.is_hot}")

# This shows that we can change the property for a particular
# object without changing the value for the class
# Showing that both exist in their own namespace
plate1.is_hot = False
print(f"Plate {plate1.is_hot}")
print(f"Meal original {Meal.is_hot}")
