'''
In this chapter I learned about good practices.. In two main topics:

    1) Efficient use of inheritence 
    2) Managing the levels of access to the data contained in objects


        Liskov substitution principle 

Base class should be interchangable with any of its subclasses without 
altering any properties of the program.



We talked about the Circle-Ellipse problem [also known as Rectangle - Square] which violates 
the Lukov substitution principle as we need to set a method setter where give us the oportunity
of changing the height and the width independently in the rectangle, and in the square we need 
to change both of them at the same time, that gives us a unconsistency inheritance beacuse we can't 
change the base class without afecting the results.
'''

# Circle Elipsisi problem 

class Rectangle:
    def __init__(self,h,w):
        self.h, self.w = h, w

    def set_h(self,h):
        self.h = h

    def set_w(self,w):
        self.w = w



class Square(Rectangle):
    def __init__(self,w):
        self.h, self.w = w, w


    # HERE IS THE INCONSISTENCY 
    def set_h(self,h):
        self.h = h
        self.w = h

    def set_w(self,w):
        self.w = w
        self.h = w


'''
Also I learned about managing data access: private attributes 

    1) Naming conventions
    2) Use @property tu customize access
    3) Overrading __getattr__() and __setattr__()
'''


class Employer:
    def __init__(self,name, new_salary):
        self._salary = new_salary

    @property # <- This is telling us that you can't change this attribute 
    def salary(self):
        return self._salary 
