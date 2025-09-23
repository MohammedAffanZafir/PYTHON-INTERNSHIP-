from abstract_class import Vehicle
class Bike(Vehicle):
    def _init_(self,n,color):
        super()._init_(n)
        self.color=color
    def start(self):
        print("Start with Kick")
class Scooty(Vehicle):
    def start(self):
        print("Self Start")
class Car(Vehicle):
    def _init_(self,n,x):
        super._init_(n)
        self.no_of_gears=6
    def start(self):
        print("start with the key")