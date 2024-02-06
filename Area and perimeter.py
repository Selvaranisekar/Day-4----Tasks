'''creae a proper member variabls inside the taskif required and use them when neccessary.
For ex. for this task create a class private variable name pi=3.141 & calculate area and perimeter'''

#define a class
class Circle:

    #Class variable
    pi=3.141

    #constructor
    def __init__(self,radius):
        self.radius=radius

    #instance method
    def area_of_circle(self):
        area=self.radius**3.141
        return area
     #instance method

    def perimeter_of_circle(self):
        perimeter=2*self.pi*self.radius
        return perimeter


if __name__=="__main__":
    circle=Circle(7)
    print("Area of circle is:", circle.area_of_circle())
    print("Perimeter of circle is:", circle.perimeter_of_circle())

'''output
Area of circle is: 451.2871252038085
Perimeter of circle is: 43.974000000000004'''
