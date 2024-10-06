from typing import List, Any
from collections.abc import Iterable, Iterator

#Aggregate Interface
class Aggregate(Iterable):
    @property
    def items(self) -> List[Any]:
        pass

#Concrete Aggregate
class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._items = []
    
    def add_item(self, item: Any) -> None:
        self._items.append(item)
        
    @property
    def items(self) -> List[Any]:
        return self._items
    
    def __iter__(self) -> Iterator:
        return ConcreteIterator(self)
    
    
class AbstractIterator(Iterator):
    def __next__(self) -> Any:
        pass

#Concrete Iterator
class ConcreteIterator(AbstractIterator):
    def __init__(self, aggregate: ConcreteAggregate):
        self._aggregate = aggregate
        self._index = 0
    
    def __next__(self) -> Any:
        if self._index < len(self._aggregate.items):
             item = self._aggregate.items[self._index]
             self._index += 1
             return item
        else:
            raise StopIteration
        

#Client code
if __name__ == "__main__":
    aggregate = ConcreteAggregate()
    aggregate.add_item("Item 1")
    aggregate.add_item("Item 2")
    aggregate.add_item("Item 3")
    print("Iteration over collection")
    iterator = iter(aggregate)
    for item in iterator:
        print(item)