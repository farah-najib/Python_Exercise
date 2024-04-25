from abc import ABC, abstractmethod
import random

class Animal():
    def __init__(self, name, age, energy_level):
        self.name = name
        self.age = age
        self.energy_level = energy_level

    # @abstractmethod
    def eat(self): pass

    def sleep(self,animal_name):
        self.energy_level += 100
        print(f'{animal_name} is sleeping and energy level is: {self.energy_level}' )

    # @abstractmethod
    def make_sound(self): pass

    def play(self, animal):

        if (isinstance(self, Herbivore) and isinstance(animal, Herbivore)) or (isinstance(self, Carnivore) and isinstance(animal, Carnivore)):
            self.energy_level -= 10
            animal.energy_level -= 10
            self.check_health()
            print(f'{self.name} is playing with {animal.name}')
        else:
            print(f"{self.name} can play with {animal.name} because it's dangerous'")

    def check_health(self):
        if self.energy_level <= 0:
            print(f'{self.name} just died')

class Carnivore(Animal):
    def __init__(self, name, age, energy_level):
        super().__init__(name, age, energy_level)

    def eat(self, animal_name):
        self.energy_level += 50
        print(f"{animal_name} is eating meat and energy level is: {self.energy_level}")

    def sleep(self, animal_name):
        super().sleep(animal_name)

    def hunt(self, prey):
        if (self.energy_level > 25):
            hunt_successful = 0.25
            if random.random() < hunt_successful:
                self.energy_level = 100
                prey.energy_level = 0
                print(f'{self.name} ate {prey.name}')
                prey.check_health()
                return True
            else:
                self.energy_level -= 25
                print(f'{self.name} tried eating {prey.name}, but {prey.name} got away.')
        else:
            print(f"{self.name} doesn't have the energy to hunt.")
        return False

# @abstractmethod
# def make_sound(self): pass

class Herbivore(Animal):
    def __init__(self, name, age, energy_level):
        super().__init__(name, age, energy_level)

    def eat(self, animal_name):
        self.energy_level += 30
        print(f"{animal_name} is eating leaves and energy level is: {self.energy_level}")

    def sleep(self, animal_name):
        super().sleep(animal_name)

    # @abstractmethod
    # def make_sound(self): pass

class Lion(Carnivore):
    def __init__(self, name, age, energy_level):
        super().__init__(name, age, energy_level)

    def sleep(self):
        super().sleep(f"{self.name} Lion")

    def eat(self):
        super().eat(f"{self.name} Lion")

    def make_sound(self):
        print('Roar')

class Giraffe(Herbivore):
    def __init__(self, name, age, energy_level):
        super().__init__(name, age, energy_level)

    def make_sound(self):
        print('. . .')

    def sleep(self):
        super().sleep(f"{self.name} Giraffe")

    def eat(self):
        super().eat(f"{self.name} Giraffe")

class Elephant(Herbivore):
    def __init__(self, name, age, energy_level):
        super().__init__(name, age, energy_level)

    def make_sound(self):
        print('Honk')

    def sleep(self):
        super().sleep(f"{self.name} Elephant")

    def eat(self):
        super().eat(f"{self.name} Elephant")

class Visitor():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'The visitor name is {self.name} and age is: {self.age}'

    def feed(self, animal):
        if isinstance(animal, Carnivore):
            print(f"{self.name} wants to feed {animal.name} but isn't allowed to.")
        else:
            if animal.energy_level > 100 :
                print(f'Dont feed {self.name} because now his energy level is {animal.energy_level}!')
            else:
                print(f'{self.name} fed {animal.name}')
                animal.eat()
class Zoo:
    def __init__(self):
        self.animals = []
        self.visitors = []

    def populate(self, *animals):
        for animal in animals:
            self.animals.append(animal)

    def open(self, *visitors):
        for visitor in visitors:
            self.visitors.append(visitor)

    def herbivore_lunchtime(self):
        for animal in self.animals:
            if isinstance(animal, Herbivore):
                animal.eat()

    def carnivore_lunchtime(self):
        for animal in self.animals:
            if isinstance(animal, Carnivore):
                animal.eat()

    def updateClock(self, current_time):
        if current_time == 23:
            current_time = 0
        else:
            current_time += 1
        return current_time

    def herbivores_left(self, animal_type: Herbivore):
        herbivore_count = 0
        for animal in self.animals:
            if isinstance(animal, animal_type):
                herbivore_count += 1
        return herbivore_count

    def visitor_feeds_animal(self):
        random_visitor = random.randint(0, len(self.visitors) - 1)
        random_animal = random.randint(0, len(self.animals) - 1)
        self.visitors[random_visitor].feed(self.animals[random_animal])

    def simulation(self):
        print(f"Welcome to Zoo Simulator!\n--- Instructions ---\nPress f and then Enter to feed an animal\nPress Enter to progress 1 hour in the simulation.\nPress q and Enter to exit the simulation. ")
        starting_time = 7
        current_time = starting_time

        while True:
            user_input = input('Make a choice: ')
            if user_input == 'q':
                print('See you next time!')
                break
            elif user_input == 'f':
                self.visitor_feeds_animal()
            elif user_input == 'o':
                # TODO Optional: Enter observer mode where the user observes the zoo for 6 hours.
                pass
            else:
                self.animal_schedule(current_time)
                for animal in self.animals:
                    animal.energy_level -= 5
                    print(f"{animal.name} has {animal.energy_level} energy left!")

                    if (animal.energy_level <= 0):
                        print(f'{animal.name} died of starvation.')
                        self.animals.remove(animal)
                    elif (animal.energy_level <= 10):
                        print(f'Feeding {animal.name} because of low energy level.')
                        animal.eat()
                    elif(animal.energy_level > 100):
                        animal.energy_level = 100

                current_time = self.updateClock(current_time)
                print(f"An hour has passed. Current time: {current_time}")

    def hunting(self):
        if self.herbivores_left(Elephant) > 2 or self.herbivores_left(Giraffe) > 2:
            random_hunter = random.randint(0, len(self.animals) - 1)
            while isinstance(self.animals[random_hunter], Herbivore):
                random_hunter = random.randint(0, len(self.animals) - 1)

            random_prey = random.randint(0, len(self.animals) - 1)
            while isinstance(self.animals[random_prey], Carnivore):
                random_prey = random.randint(0, len(self.animals) - 1)

            if self.herbivores_left(type(self.animals[random_prey])) > 2:
                hunt_successful = self.animals[random_hunter].hunt(self.animals[random_prey])
                if hunt_successful:
                    self.animals.remove(self.animals[random_prey])
                return True
            else:
                print(f"{self.animals[random_hunter].name} wasn't allowed to hunt {self.animals[random_prey].name} because {self.animals[random_prey].name} is endangered.")
        else:
            return False

    def playing(self):
        random_player_1 = random.randint(0, len(self.animals) - 1)
        random_player_2 = random.randint(0, len(self.animals) - 1)
        while random_player_1 == random_player_2:
            random_player_2 = random.randint(0, len(self.animals) - 1)
        self.animals[random_player_1].play(self.animals[random_player_2])

    # Put animal scheduling code in separate method
    def animal_schedule(self, current_time):

        if current_time == 8 or current_time == 12 or current_time == 15 or current_time == 20: # FOOD Time: 8AM, 12PM, 15PM, 19PM
            print('Food Time..')
            self.carnivore_lunchtime()
            self.herbivore_lunchtime()

        if (current_time > 9 and current_time < 11) or (current_time >= 16 and current_time < 17):      # Play Time between 9-11 and 15-17
            # TODO play
            for animal in self.animals:
                    print("Play time.. ")
                    animal.play(animal)

        if current_time >=17 and current_time <=18:     # HUNTING Time: 17:00-18:00
            print('Hunting Time..')
            hunting_happened = self.hunting()
            if not hunting_happened:
                print("There aren't enough herbivores left so the carnivores are kept from hunting. ")


        if current_time >= 21 or current_time <= 6:      # SLEEP Time: 21-6:00
            for animal in self.animals:
                print("Sleeping time..")
                animal.sleep()

        # progress time between 22 and morning
def main():
    zoo = Zoo()

    simba = Lion("Simba", 3, 30)
    Dimba = Lion("Dimba", 4, 30)
    dumbo = Elephant('Dumbo', 5, 60)
    Lumbo = Elephant('Lumbo', 6, 60)
    adira = Elephant('Adira', 8, 60)
    melman = Giraffe('Melman', 5, 60)
    belman = Giraffe('Belman', 7, 60)
    zarafa = Giraffe('Zarafa', 9, 60)

    zoo.populate(simba, dumbo, melman, adira, zarafa, dumbo, Lumbo, belman)

    john = Visitor('John', 32)
    mary = Visitor('Mary', 36)
    zoo.open(john, mary)

    zoo.simulation()

main()
