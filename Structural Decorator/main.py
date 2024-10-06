from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass
    
    @abstractmethod
    def description(self) -> str:
        pass
    

class BasicCoffee(Coffee):
    def cost(self) -> float:
        return 5.0
    
    def description(self) -> str:
        return "Basic Coffee"
    
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    
    def cost(self) -> float:
        return self._coffee.cost()
    
    def description(self) -> str:
        return self._coffee.description()
    
class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 2.0
    
    def description(self) -> str:
        return super().description() + ", milk"
    
class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 1.0
    
    def description(self) -> str:
        return super().description() + ", sugar"
    
    
#Client code
if __name__ == "__main__":
    
    my_coffee = BasicCoffee()
    print(f"Cost: {my_coffee.cost()}, Decription: {my_coffee.description()}")
    
    my_coffee = MilkDecorator(my_coffee)
    print(f"Cost: {my_coffee.cost()}, Decription: {my_coffee.description()}")
    
    my_coffee = SugarDecorator(my_coffee)
    print(f"Cost: {my_coffee.cost()}, Decription: {my_coffee.description()}")