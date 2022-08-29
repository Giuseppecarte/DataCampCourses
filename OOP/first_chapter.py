"""
In this first chapter we saw the anatomy of a class, what a class contains and how those 
things inside a class behave.

Mainly we have to things that are:
 1. Attributes 
 2. Methods 

How to call an attribute:
obj.my_attribute (like a variable)

How to call a method:
obj.my_method() (like a function)


Also the most powerfull thing that I understood was the *self* word which I've been struggling to understand
and it seems that is pretty easy haha the *self* word it's just to generalize everything in your class, as
the class is just a templeate and when you instanciate the class you can choose the name of that object as wanted 
the *self* word is what python uses to reference everything that your class have with the object name

At last we build a class from scratch with all that this chapter teached to us.
"""
# Write the class Point as outlined in the instructions
class Point:

    def __init__(self,x = 0.0,y = 0.0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        leg1_squared = self.x ** 2
        leg2_squared = self.y ** 2 
        hypotenuse   = (leg1_squared + leg2_squared) ** (1/2)
        return hypotenuse
    
    def reflect(self, axis = 'x'):
        if axis == 'x':
            self.y = -1 * self.y
        if axis == 'y':
            self.x = -1 * self.x
        else:
            raise Exception('Invalid axis')

pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())