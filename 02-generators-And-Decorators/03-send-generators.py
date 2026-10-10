def meal_customer():
    print("Welcome! What do you want to eat today?")
    order = yield
    while True:
        print(f"Preparing {order}")
        # This order stops the generator and waits for the next order
        # otherwise we enter an infinite loop and the generator will not stop
        order = yield


stall = meal_customer()
next(stall)  # starting the generator

# stall.send("Butter Chicken")  # sending the first order

take_order_input = input("Please enter your order: ")
stall.send(take_order_input)
