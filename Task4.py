class Person:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        return self.weight / (self.height ** 2)

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.weight == other.weight and self.height == other.height
        return False

# Contoh Penggunaannya:
person1 = Person(weight=70, height=1.75)
person2 = Person(weight=70, height=1.75)
person3 = Person(weight=80, height=1.80)

print(person1.BMI_Value())  # Output: 22.85
print(person1 == person2)  # Output: True
print(person1 == person3)  # Output: False