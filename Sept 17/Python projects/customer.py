class Customer:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def greet(self):
        return f"Hello my name is {self.firstname}{self.lastname} and iam {self.age} years old."
c1 = Customer("Rahul", "Sharma", 32)
c2 = Customer("Priya", "Warrier", 21)

print(c1.greet())
print(c2.greet())