class Rectangle(object):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area (self):
        return self.length*self.width
class Square(Rectangle):
    def __init__(self, width):
        self.length=width
        self.width=width
class Ellipse(object):
    π=3.1415926
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area (self):
        return self.π*self.a*self.b
class Circle(Ellipse):
    def __init__(self,r):
        self.a=r
        self.b=r
    def compute_area(shapes):
    s=0
    for shape in shapes:
        s+=shape.area()
    return s
shapes = [Ellipse(10, 20), Square(15), Circle(5),
          Rectangle(20, 15), Circle(5), Square(15),
          Ellipse(10, 20)]
total_area=compute_area(shapes)
print(total_area)
        

