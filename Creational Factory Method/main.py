from abc import ABC, abstractmethod

class Pet(ABC):
    
    @abstractmethod
    def speak(self):
        pass
    
    
class Dog(Pet):
    def speak(self):
        return "Woof!"

class Cat(Pet):
    def speak(self):
        return "Meow!"
    
class Bird(Pet):
    def speak(self):
        return "Chirp!"
    

#Define a pet shop
class PetShop(ABC):
    @abstractmethod
    def create_pet(self):
        pass
    
#Concrete Petshop that implement factory method
class DogShop(PetShop):
    def create_pet(self):
        return Dog()


class CatShop(PetShop):
    def create_pet(self):
        return Cat()



class BirdShop(PetShop):
    def create_pet(self):
        return Bird()
    

#Test factory method
def pet_speak(petshop):
    pet = petshop.create_pet()
    print(f"The pet says {pet.speak()}")
    

#Create a dog shop
pet_speak(DogShop())


#Create a cat shop
pet_speak(CatShop())


#Create a bird shop
pet_speak(BirdShop())
    
    
        