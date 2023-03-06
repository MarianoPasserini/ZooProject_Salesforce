import datetime

class Animals:
    def __init__(self,animal_species, name, gender, number_of_legs):
        self.animal_species = animal_species
        self.name = name
        self.number_of_legs = number_of_legs
        self.gender = gender

    def show_animals(self):
        animal_info = "Species: {}, Name: {}, Number of legs: {}, Gender: {}".format(self.animal_species, self.name, self.number_of_legs, self.gender)
        if isinstance(self, Giraffe):
            animal_info += ", Height: {}".format(self.height)
        elif isinstance(self, Crocodile):
            animal_info += ", Number of teeth: {}".format(self.number_of_teeth)
        elif isinstance(self, GiantTortoise):
            animal_info += ", Age: {} years".format(self.age)
        return animal_info
    
    
class Giraffe(Animals):
    def __init__(self, animal_species, name, gender,  number_of_legs, height):
        super().__init__(animal_species, name, gender, number_of_legs)
        self.height = f"{height} m"
    def compare_height(self): #here i compare the height of the giraffe to the average height of a giraffe.
        if self.gender == "male":
            avg_height = 5.5
        else:
            avg_height = 4.6
        if self.height > avg_height:
            return f"{self.name} is taller than the average {self.gender} giraffe."
        elif self.height < avg_height:
            return f"{self.name} is shorter than the average {self.gender} giraffe."
        else:
            return f"{self.name} is the average height for a {self.gender} giraffe."
        
class Crocodile(Animals):
    def __init__(self, animal_species, name, gender,  number_of_legs, number_of_teeth):
        super().__init__(animal_species, name, gender,  number_of_legs)
        self.number_of_teeth = number_of_teeth
    def favorite_food(self, food):
        print(f"{self.name} loves to eat {food}.")

class GiantTortoise(Animals):
    def __init__(self, animal_species, name, gender,  number_of_legs, age):
        super().__init__(animal_species, name, gender,  number_of_legs)
        self.age = age
    def get_age(self):
        if self.age < 50:
            return f"{self.name} is a young tortoise."
        elif self.age > 50 and self.age < 100:
            return f"{self.name} is an middle-aged tortoise."
        else:
            return f"{self.name} is an old tortoise."
        
class Zoo:
    def __init__(self, name, city, operating_hours): #1) a. Create Zoo class with the indicated parameters and attributes.
        self.name = name
        self.city = city
        self.operating_hours = operating_hours
        self.animals = []

    def add_animal(self, animal): #b) ii. Add animals to the zoo.
        self.animals.append(animal)

    def number_of_animals(self): #b) i. Print the number of animals in the zoo.
        return len(self.animals)
    
    def remove_animal(self, animal): #b) iii. Remove animals from the zoo.
        self.animals.remove(animal)

    def print_animals(self): #b) iv. Print the information about the animals in the zoo.
        for animal in self.animals:
            print(animal.show_animals())

    def admission_price(self, day_of_week=None): #b) v. Print the admission price for today. (The fancy way using datetime and a default parameter)
        if day_of_week is None:
            day_of_week = datetime.datetime.today().weekday()
        if day_of_week in [0, 1, 3, 4]:
            return 19.99
        elif day_of_week == 2:
            return 9.99
        else:
            return 25.99

    
    # def admission_price(self, day_of_week): #b) v. Print the admission price for today. (The easy way)
    #     if day_of_week in [0, 1, 3, 4]:
    #         return 19.99
    #     elif day_of_week == 2:
    #         return 9.99
    #     else:
    #         return 25.99
            
# create a new zoo
zoo = Zoo("My Zoo", "New York City", "9AM - 6PM")

# create some animals
giraffe1 = Giraffe("Giraffe", "Gerald", "male", 4, 5.7)
giraffe2 = Giraffe("Giraffe", "Gigi", "female", 4, 4.3)
crocodile = Crocodile("Crocodile", "Charlie", "male", 4, 80)
tortoise = GiantTortoise("Tortoise","Richard","Male",4, 150)

# add animals to the zoo
zoo.add_animal(giraffe1)
zoo.add_animal(giraffe2)
zoo.add_animal(crocodile)
zoo.add_animal(tortoise)

# print the number of animals in the zoo
print(zoo.number_of_animals())
# print the zoo animals
zoo.print_animals()

# remove an animal from the zoo
zoo.remove_animal(giraffe1)

# print the number of animals in the zoo and the info about the animals again to make sure the animal was removed
print(zoo.number_of_animals())
zoo.print_animals()
# print the admission price for today
print(f"The admission price for today is: ${zoo.admission_price()}")

    

