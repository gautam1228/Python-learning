class DrinkOrder:

    def __init__(self, beverage_type, sweetness, quantity):
        self.beverage_type = beverage_type
        self.sweetness = sweetness
        self.quantity = quantity

    # Class methods are generally used as alternate constructors
    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["beverage_type"],
            order_data["sweetness"],
            order_data["quantity"],
        )

    @classmethod
    def from_string(cls, order_string):
        beverage_type, sweetness, quantity = order_string.split("-")
        return cls(beverage_type, sweetness, quantity)

    # Static methods are generally independent utilities / helpers
    @staticmethod
    def is_valid_sweetness(sweetness):
        return sweetness in ["Very Sweet", "Sweet", "Regular", "Less Sweet", "No Sugar"]


order1 = DrinkOrder.from_dict(
    {"beverage_type": "Kokum Soda", "sweetness": "Regular", "quantity": "4"}
)

order2 = DrinkOrder.from_string("Buttermilk-No Sugar-2")

print(order1.__dict__)
print(order2.__dict__)
