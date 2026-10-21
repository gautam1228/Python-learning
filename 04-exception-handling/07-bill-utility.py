class InvalidDrinkError(Exception):
    pass


def bill(flavour, glasses):
    menu = {"Fresh Lime Soda": 70, "Kokum Soda": 30, "Banana Milk": 60}

    try:
        if flavour not in menu:
            raise InvalidDrinkError("We do not serve that drink.")
        if not isinstance(glasses, int):
            raise TypeError("Number of glasses must be an integer.")
        total_cost = menu[flavour] * glasses
        print(f"Your bill for {glasses} glasses of {flavour} is rupees {total_cost} ")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Thank you for visiting our shop !")


bill("Soda", 3)
bill("Kokum Soda", "four")
bill("Banana Milk", 7)
