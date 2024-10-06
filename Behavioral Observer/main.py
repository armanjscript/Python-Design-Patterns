from abc import ABC, abstractmethod
from typing import List, Any

#Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, message: Any) -> None:
        pass

#Subject Interface
class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def notify_observers(self) -> None:
        pass
    
#Concrete Subject
class ConcreteSubject(Subject):
    def __init__(self, state: int):
        self._state = state
        self._observers: List[Observer] = []
        
    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._state)
            
    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)
        
            
    def set_state(self, state: int) -> None:
        self._state = state
        self.notify_observers()
        
#Concrete Observer
class ConcreteObserver(Observer):
    def __init__(self, name:str):
        self._name = name
    def update(self, message: Any) -> None:
        print(f"Observer {self._name} recieved message: {message}")
        
#Client code 
if __name__ == "__main__":
    subject = ConcreteSubject(0)
    
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")
    
    subject.add_observer(observer1)
    subject.add_observer(observer2)
    
    subject.set_state(1)
    
    subject.remove_observer(observer1)
    subject.set_state(2)
    
    
    