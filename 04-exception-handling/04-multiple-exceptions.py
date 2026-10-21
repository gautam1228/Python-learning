def process_order(item, quantity):

    try:
        price = {"mocktail": 120}[item]
        total_cost = int(price) * int(quantity)

        print(f"Total cost is {total_cost}")
    except KeyError:
        print("We don't serve that item !")
    except ValueError:
        print("Quantity needs to be an integer.")


process_order("mocktail", 5)
process_order("soda", 4)
process_order("mocktail", "four")
