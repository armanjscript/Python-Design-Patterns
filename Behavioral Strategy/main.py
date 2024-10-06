from typing import List, Type
from abc import ABC, abstractmethod


#Strategy interface
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, dataset: List[int]) -> List[int]:
        pass
    
#Concrete Strategy
class BubbleSort(SortingStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        
        n = len(dataset)
        for i in range(n):
            for j in range(0, n-i-1):
                if dataset[j] > dataset[j+1]:
                    dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
        return dataset
    

class QuickSort(SortingStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        if len(dataset) <= 1:
            return dataset
        pivot = dataset[len(dataset) // 2]
        left = [x for x in dataset if x < pivot]
        middle = [x for x in dataset if x == pivot]
        right = [x for x in dataset if x > pivot]
        return self.sort(left) + middle + self.sort(right)
    
    

#Context
class SortedList:
    def __init__(self, strategy: Type[SortingStrategy]):
        self._dataset = []
        self._strategy = strategy()
        
    def add(self, value: int):
        self._dataset.append(value)
    
    def sort(self) -> List[int]:
        return self._strategy.sort(self._dataset)
        
        
#Client code

if __name__ == "__main__":
    
    #Using BubbleSort Strategy
    bubble_sorted_list = SortedList(BubbleSort)
    bubble_sorted_list.add(3)
    bubble_sorted_list.add(1)
    bubble_sorted_list.add(4)
    bubble_sorted_list.add(1)
    bubble_sorted_list.add(5)
    print("Bubble Sorted List:", bubble_sorted_list.sort())
    
    #Using QuickSort Strategy
    quick_sorted_list = SortedList(QuickSort)
    quick_sorted_list.add(3)
    quick_sorted_list.add(1)
    quick_sorted_list.add(4)
    quick_sorted_list.add(1)
    quick_sorted_list.add(5)
    print("Quick Sorted List:", quick_sorted_list.sort())


