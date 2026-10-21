def cook_meal(dish):
    if dish not in ["Butter chicken", "Sushi", "Kimchi"]:
        raise ValueError("We do not serve that dish :)")
    print(f"Serving * {dish} * now ...")


cook_meal("Sushi")
cook_meal("French Fries")
