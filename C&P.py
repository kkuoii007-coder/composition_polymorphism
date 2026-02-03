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

def make_animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Person:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def care(self):
        print(f"{self.name} заботится о животных")

class ZooKeeper(Person):
    def __init__(self, name, nationality):
        super().__init__(name, nationality)

    def feed_animal(self):
        print(f"{self.name} покормил животное")

class Veterinarian(Person):
    def __init__(self, name, nationality):
        super().__init__(name, nationality)

    def heal_animal(self):
        print(f"{self.name} излечил животное")

class Zoo:
    def __init__(self):
        self.animals = []
        self.persons = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_person(self, person):
        self.persons.append(person)

    def show_animals(self):
        print("\nЖивотные в зоопарке:")
        for animal in self.animals:
            print(f"- {animal.__class__.__name__}: name={animal.name}, age={animal.age}")

    def show_persons(self):
        print("\nСотрудники зоопарка:")
        for per in self.persons:
            print(f"- {per.__class__.__name__}: name={per.name}, nationality={per.nationality}")



zoo = Zoo()

bird = Bird("Кеша", 2, "green")
mammal = Mammal("Барсик", 5, 4.2)
reptile = Reptile("Гоша", 3, "desert")

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

keeper = ZooKeeper("Паша", "RU")
vet = Veterinarian("Ольга", "RU")

zoo.add_person(keeper)
zoo.add_person(vet)

make_animal_sound(zoo.animals)

zoo.show_animals()
zoo.show_persons()

print("\nДействия сотрудников:")
keeper.care()
keeper.feed_animal()
vet.care()
vet.heal_animal()
