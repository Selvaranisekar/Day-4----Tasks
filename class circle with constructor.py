''' Create a python class called circle with constructor which will take a list as an argument
for the task.
the List is [10,501,22,37,100,999,87,351]'''

#define a class

class circle:
    List=[10,501,22,37,100,999,87,351]

#constructor
    def __init__(self):
        self.list=list
#instance method
    def num_list(self):
        l=self.List
        return l

if __name__=="__main__":
    c=circle()
    print(circle.List)

'''output
[10, 501, 22, 37, 100, 999, 87, 351]'''


