

#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} ест")

    def make_sound(self):
        print(f"{self.name} издает звук")

class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print(f"{self.name} издает тихий звук")

class Mammal(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight

    def make_sound(self):
        print(f"{self.name} издает громкий звук")

class Reptile(Animal):
    def __init__(self, name, age, area):
        super().__init__(name, age)
        self.area = area

    def make_sound(self):
        print(f"{self.name} не издает звук")

bird1 = Bird("Грего", 5, "красный")
bird1.eat()
bird1.make_sound()