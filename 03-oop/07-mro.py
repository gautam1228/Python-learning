class A:
    label = "A: Base Class"


class B(A):
    label = "B: Coffee Class"


class C(A):
    label = "C: Chai Class"


class D(C, B):
    pass


print(D.label)  # prints -> C: Chai Class

# Why ?
# Because of the MRO of class D (MRO: Method Resolution Order)

print(D.__mro__)
