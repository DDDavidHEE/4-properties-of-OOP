# Định nghĩa lớp Animal thể hiện 4 thuộc tính của OOP

# 1. Encapsulation (Đóng gói)
class Animal:
    def __init__(self, name, species):
        self.name = name        # Thuộc tính công khai
        self.__species = species  # Thuộc tính riêng tư (Encapsulation)

    def get_species(self):
        return self.__species  # Getter để truy cập thuộc tính riêng tư

# 2. Inheritance (Kế thừa)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Gọi constructor của lớp cha
        self.breed = breed

    # 3. Polymorphism (Đa hình)
    def make_sound(self):
        return "Woof! Woof!"

# 4. Abstraction (Trừu tượng)
from abc import ABC, abstractmethod

class AnimalSound(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal, AnimalSound):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def make_sound(self):
        return "Meow! Meow!"

# Chạy thử chương trình
if __name__ == "__main__":
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers")

    print(f"{dog.name} is a {dog.get_species()} and makes sound: {dog.make_sound()}")
    print(f"{cat.name} is a {cat.get_species()} and makes sound: {cat.make_sound()}")
