class Toddler:

    def __init__(self, age):
        self._age = age

    # Getter
    @property
    def age(self):
        return self._age + 2

    # Setter
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Toddler's age must be between 1 and 5 years")


toddler1 = Toddler(3)
print(toddler1.age)

toddler1.age = 5
print(toddler1.age)

toddler1.age = 7  # raises an error
