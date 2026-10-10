def serve_meals():
    yield "#Server Meal 1"
    yield "#Server Meal 2"
    yield "#Server Meal 3"


stall = serve_meals()

for meal in stall:
    print(meal)


def get_meal_list():
    return ["Meal 1", "Meal 2", "Meal 3"]


# Generator function
def get_meal_gen():
    yield "Meal 1"
    yield "Meal 2"
    yield "Meal 3"


meal = get_meal_gen()
# print(meal)
print(next(meal))
print(next(meal))
print(next(meal))
# print(next(meal)) # Gives error as there are no more items to yield
