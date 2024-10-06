from abc import ABC, abstractmethod
from typing import List, Dict


class Investor(ABC):
    @abstractmethod
    def update(self, stock: str, price: float) -> None:
        pass
    
#Subject Interface
class StockMarket(ABC):
    @abstractmethod
    def register_investor(self, investor: Investor, stock: str) -> None:
        pass
    
    @abstractmethod
    def remove_investor(self, investor: Investor, stock: str) -> None:
        pass
    
    @abstractmethod
    def notify_investor(self, stock: str) -> None:
        pass
    
#Concrete Subject
class ConcreteStocckMarket(StockMarket):
    def __init__(self):
        self._stocks: Dict[str, float] = {}
        self._investors: Dict[str, List[Investor]] = {}
        
    def register_investor(self, investor: Investor, stock: str) -> None:
        if stock not in self._investors:
            self._investors[stock] = []
        self._investors[stock].append(investor)
        
    def remove_investor(self, investor: Investor, stock: str) -> None:
        self._investors[stock].remove(investor)
        
    def notify_investor(self, stock: str) -> None:
        for investor in self._investors.get(stock, []):
            investor.update(stock, self._stocks[stock])
            
    def set_stock(self, stock: str, price: float):
        self._stocks[stock] = price
        self.notify_investor(stock)

#Concrete Observer
class ConcreteInvestor(Investor):
    def __init__(self, name: str) -> None:
        self._name = name
    
    def update(self, stock: str, price: float) -> None:
        print(f"Investor {self._name} notified. Stock: {stock}, New Price: {price}")
        


#Client code

if __name__ == "__main__":
    stock_market = ConcreteStocckMarket()
    investor1 = ConcreteInvestor("Alice")
    investor2 = ConcreteInvestor("Bob")
    
    stock_market.register_investor(investor1, "AAPL")
    stock_market.register_investor(investor1, "GOOGLE")
    stock_market.register_investor(investor2, "AAPL")
    
    stock_market.set_stock("AAPL", 150.0)
    stock_market.set_stock("GOOGLE", 153.4)
    
        