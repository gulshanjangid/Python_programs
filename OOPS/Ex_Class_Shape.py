class shape:
    def __init__(self):
       pass

    def area(self):
         return 0
     
class Square(shape):
    def __init__(self,length):
        super().__init__()
        self.length =length

class Circle(shape):
    pass

    def area(self):
        return self.length**2 
    
    shape = shape()
s = Square(int(input("Enter the length of the square: ")))
print("The area of the square is:", s.area())

           