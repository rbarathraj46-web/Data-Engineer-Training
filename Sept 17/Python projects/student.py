class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello my name is {self.name} and iam {self.age} years old."
s1 = Student("Rahul", 21)
s2 = Student("Priya", 22)

print(s1.greet())
print(s2.greet())
