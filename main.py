from abc import ABC, abstractmethod


# Abstraction & Inheritance
class Animal(ABC):
    def __init__(self, name): self.name = name

    @abstractmethod
    def make_sound(self): pass


class Dog(Animal):
    def make_sound(self): return "Woof!"


class Cat(Animal):
    def make_sound(self): return "Meow!"


# Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0: self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance: self.__balance -= amount

    def get_balance(self):
        return self.__balance


# Testing
if __name__ == "__main__":
    dog, cat = Dog("Buddy"), Cat("Whiskers")
    print(f"{dog.name} says: {dog.make_sound()}")
    print(f"{cat.name} says: {cat.make_sound()}")

    account = BankAccount("Alice", 1000)
    account.deposit(500)
    account.withdraw(300)
    print(f"Final balance: {account.get_balance()}")
