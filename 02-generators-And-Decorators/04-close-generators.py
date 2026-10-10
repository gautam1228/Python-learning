def make_meals():
    yield "Meal 1 is ready"
    yield "Meal 2 is ready"


def make_drinks():
    yield "Drink 1 is ready"
    yield "Drink 2 is ready"


def make_food():
    yield from make_meals()
    yield from make_drinks()


for food_item in make_food():
    print(food_item)


def food_stall():
    try:
        while True:
            yield "Waiting for food order"
    except:
        print("No more food, we're closed :)")


stall = food_stall()
print(next(stall))
stall.close()  # good practice to always close generators, gracefully stops the generator
