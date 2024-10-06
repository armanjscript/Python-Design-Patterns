from abc import ABC, abstractmethod


#Define Animal interface 
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
#Concrete implementations for different type of animals
class Lion(Animal):
    def sound(self):
        return "Roar!"


class Tiger(Animal):
    def sound(self):
        return "Growl!"


class Snake(Animal):
    def sound(self):
        return "Hiss!"


class Crocodile(Animal):
    def sound(self):
        return "Bellow!"
    
    
#Define the animal factory
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self, animal_type):
        pass
    
    
class MamalFactory(AnimalFactory):
    def create_animal(self, animal_type):
        if animal_type == "Lion":
            return Lion()
        elif animal_type == "Tiger":
            return Tiger()
        else:
            raise ValueError("Invalid animal type")


class ReptileFactory(AnimalFactory):
    def create_animal(self, animal_type):
        if animal_type == "Snake":
            return Snake()
        elif animal_type == "Crocodile":
            return Crocodile()
        else:
            raise ValueError("Invalid animal type")
        
        
#Function to demonstrate Abstract Factory Pattern
def animal_sound(factory, animal_type):
    animal = factory.create_animal(animal_type)
    print(f"The {animal_type} goes: {animal.sound()}")
    
    
#Create a mamal factory and get the sounds of its animals
animal_sound(MamalFactory(), 'Lion')
animal_sound(MamalFactory(), 'Tiger')

#Create a reptile factory and get the sounds of its animals
animal_sound(ReptileFactory(), 'Snake')
animal_sound(ReptileFactory(), 'Crocodile')

    
    
        
    
