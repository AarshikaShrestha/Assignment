class Animal:
    def __init__(self, name, species, age, feeding_time):
        self.name = name
        self.species = species
        self.age = age
        self.feeding_time = feeding_time

    def update_feeding_time(self, new_time):
        self.feeding_time = new_time

    def matches(self, keyword):
        return keyword.lower() in self.name.lower() or keyword.lower() in self.species.lower()

    def __str__(self):
        return f"{self.name} ({self.species}), Age: {self.age}, Feeding Time: {self.feeding_time}"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, name, species, age, feeding_time):
        animal = Animal(name, species, age, feeding_time)
        self.animals.append(animal)
        print(f"{name} the {species} has been added to the zoo.\n")

    def list_animals(self):
        if not self.animals:
            print("No animals in the zoo.\n")
            return
        print("Zoo Animals:")
        for animal in self.animals:
            print(animal)
        print()

    def search_animals(self, keyword):
        results = [animal for animal in self.animals if animal.matches(keyword)]
        if results:
            for animal in results:
                print(animal)
        else:
            print("No matching animals found.")
        print()

    def update_feeding_time(self, name, new_time):
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                animal.update_feeding_time(new_time)
                print(f"Feeding time for {name} updated to {new_time}.\n")
                return
        print("Animal not found.\n")


def zoo_menu():
    zoo = Zoo()

    while True:
        print("Zoo Menu:")
        print("1. Add Animal")
        print("2. List Animals")
        print("3. Search Animal")
        print("4. Update Feeding Time")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            species = input("Species: ")
            age = input("Age: ")
            feeding_time = input("Feeding Time: ")
            zoo.add_animal(name, species, age, feeding_time)
        elif choice == "2":
            zoo.list_animals()
        elif choice == "3":
            keyword = input("Enter name or species: ")
            zoo.search_animals(keyword)
        elif choice == "4":
            name = input("Enter name of animal: ")
            new_time = input("Enter new feeding time: ")
            zoo.update_feeding_time(name, new_time)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


zoo_menu()
