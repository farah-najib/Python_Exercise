import random
class Animal :
    def __init__(self, name, age,energy_level):
        self.name = name
        self.age = age
        self.energy_level = energy_level

    def eat(self): pass

    def sleep(self,animal_name):
        self.energy_level+=100
        print(f'{animal_name} is sleeping and energy level is: {self.energy_level}' )
    def make_sound(self): pass

    def play(self, animal):
        if (isinstance(self, Herbivore) and isinstance(animal, Herbivore)) or (isinstance(self, Carnivore) and isinstance(animal, Carnivore)):
            self.energy_level -= 10
            animal.energy_level -= 10
            self.check_health()
            print(f'{self.name} is playing with {animal.name}')
        else:
            print(f"{self.name} can not play with {animal.name} because it's dangerous'")

    def check_health(self):
        if self.energy_level <= 0:
            print(f'{self.name} just died')

class Carnivore(Animal):
    def __init__(self, name, age, energy_level):
        super().__init__(name, age, energy_level)

    def eat(self, animal_name):
        self.energy_level += 10
        print(f"{animal_name} is eating meat and energy level is: {self.energy_level}")

    def sleep(self, animal_name):
        super().sleep(animal_name)

    def hunt(self, prey):
        hunt_successful = 0.25
        if random.random() < hunt_successful:
            self.energy_level = 100
            prey.energy_level = 0
            print(f'{self.name} ate {prey.name}')
            prey.check_health()
        else:
            self.energy_level -= 25
            print(f'{self.name} tried eating {prey.name}, but {prey.name} got away.')

class Herbivore(Animal):
    def __init__(self, name, age, energy_level):
        super().__init__(name, age, energy_level)

    def eat(self, animal_name):
        self.energy_level += 10
        print(f"{animal_name} is eating leaves and energy level is: {self.energy_level}")

    def sleep(self, animal_name):
        super().sleep(animal_name)


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


    def playtime(self):
        print("Playing time")
        if len(self.animals) >= 2:
                animal1, animal2 = random.sample(self.animals, 2)
                animal1.play(animal2)
        else:
                print("There are not enough animals in the zoo for playtime.")


    def hunting_time(self):
        print("hunting time")
        for animal in self.animals:
            if isinstance(animal, Carnivore):
                prey = random.choice([a for a in self.animals if isinstance(a, Herbivore) and a.energy_level > 0])
                if prey:
                    animal.hunt(prey)

    def updateClock(self,current_time):
         if current_time == 23:
            current_time = 0
         else:
            current_time += 1

         return current_time

    def visitor_feeds_animal(self):
       random_visitor = random.randint(0, len(self.visitors) - 1)
       random_animal = random.randint(0, len(self.animals) - 1)
       self.visitors[random_visitor].feed(self.animals[random_animal])



    def animal_schedule(self,current_time):
        if current_time < 12:
           pass
        if current_time == 12:
           self.herbivore_lunchtime()
        if current_time == 13:
           self.carnivore_lunchtime()
        elif 14 <= current_time < 17:
            self.playtime()
        elif 17 <= current_time < 20:
             self.hunting_time()
        if current_time == 22:
           for animal in self.animals:
             animal.sleep()

    # progress time between 22 and morning


    # Added a simple user interface
    def zoo_simulation(self):
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
                pass
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
                        #self.animals = updateAnimalsList(self.animals)
                    elif (animal.energy_level <= 10):
                        print(f'Feeding {animal.name} because of low energy level.')
                        animal.eat()

            current_time = self.updateClock(current_time)
            print(f"An hour has passed. Current time: {current_time}")





zoo = Zoo()
simba = Lion("Simba", 3, 30)
dumbo = Elephant('Dumbo', 5, 60)
melman = Giraffe('Melman', 5, 60)
zoo.populate(simba, dumbo, melman)
john = Visitor('John', 32)
mary = Visitor('Mary', 36)
zoo.open(john, mary)
zoo.zoo_simulation()
