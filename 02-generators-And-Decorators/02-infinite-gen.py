def get_meals():
    count = 1
    while True:
        yield f"Meal #{count}"
        count += 1


meal_shop = get_meals()
meal_shop_2 = get_meals()  # works independently

for _ in range(5):
    print(next(meal_shop))

for _ in range(3):
    print(next(meal_shop))  # continues from the point where it left off

for _ in range(3):
    print(next(meal_shop_2))
