drink_ingredients = {"soda": 30, "mocktail_syrup": 40}

try:
    drink_ingredients["quantity"]
except KeyError:
    print("The key you're trying to access doesn't exist.")
