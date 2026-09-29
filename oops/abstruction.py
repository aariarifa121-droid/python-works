
from abc import ABC,abstractmethod

class shape(ABC):

    @abstractmethod
    def get_area(self):

        pass


    @abstractmethod
    def get_perimeter(self):
        pass


        
class rectangle(shape):

    def __init__(self):
        self.length = int(input("enter length"))
        self.breadth = int(input("enter breadth"))


    def get_area(self):

        print("area",self.length*self.breadth)    


    def get_perimeter(self):
        print("perimeter",2*(self.length+self.breadth))


r = rectangle()

r.get_perimeter()
r.get_area()


class square(shape):

    def __init__(self):
        self.length = int(input("enter length"))
        self.breadth = int(input("enter breadth"))


    def get_area(self):

        print("area",self.length*self.breadth)    


    def get_perimeter(self):
        print("perimeter",2*(self.length+self.breadth))


s = square()

s.get_perimeter()
s.get_area()



