
# Parent class
class Animal:

    def eat(self):
        print("Animal is eating")


# Child class
class Dog(Animal):

    def bark(self):
        print("Dog is barking")


# Main program
d = Dog()

d.eat()   # Inherited method
d.bark()  # Child class method
