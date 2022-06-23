# Multiple Inheritance
from abc import ABC, abstractmethod
class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass

# Decorator
def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]

    return inner

@decorator_list
def add_together(a, b):
    return a + b

# Abstract class
class Animal(ABC):

    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark")


class Lion(Animal):

    def move(self):
        print("I can roar")


# Driver code
print("Abstract Class Implementation")
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()

print("Decorator Implementation")
print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))

print("Multiple Inheritance Implementation")
obj = Class4()
obj.m()
