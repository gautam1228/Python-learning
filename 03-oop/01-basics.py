class Meal:
    pass


class MealTime:
    pass


print(type(Meal))

new_meal = Meal()

print(new_meal.__class__)
print(type(MealTime))
print(type(new_meal) is Meal)
print(type(new_meal) is MealTime)
