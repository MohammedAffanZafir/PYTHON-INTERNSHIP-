from abc import ABC,abstractmethod
class Vehicle(ABC):
    def _init_(self,n):
        self.no_of_tyres=n
    @abstractmethod
    def start(self):
        pass
    def manfac(self):
        pass
    def display(self):
        print("Hi i am calling from vehicle class")