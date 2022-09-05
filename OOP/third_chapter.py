'''
We started the third chapter with the next question .... ***
'''
class Customer:
    def __init__(self,name, balance, id):
        self.name = name
        self.balance = balance 
        self.id = id 


name = 'Giuseppe'
balance = 1000
customer_id = 1234 

Customer1 = Customer(name, balance, customer_id)
Customer2 = Customer(name, balance, customer_id)
print(Customer1 == Customer2) # <---- Why this is False if they are the same customer?? ***
print(Customer1) #<__main__.Customer object at 0x000001D142D47D60> <-- reference to that memory chunk (1)
print(Customer2) #<__main__.Customer object at 0x000001D142F14550> <-- 

'''
Adding the __eq__() method makes that when calling the == operator point to the __eq__() insted of looking at
the memory chunk where the objects are saved.

Other Examples as in Haskell:
1. == -> __eq__()
2. != -> __ne__()
3. >= -> __ge__()
4. <= -> __le__()
5. >  -> __gt__()
6. <  -> __lt__()
7.       __hash__() to use your objects as  dictionary keys and in sets 
'''
class Customer:
    def __init__(self,name, balance, id):
        self.name = name
        self.balance = balance 
        self.id = id 
    def __eq__(self, other):
        return (self.id == other.id) and (self.name == other.name)
    

name = 'Giuseppe'
balance = 1000
customer_id = 1234 

Customer1 = Customer(name, balance, customer_id)
Customer2 = Customer(name, balance, customer_id)
print(Customer1 == Customer2) # <---- it returns True  

'''
The next interesting part is how to print in the console the object insted of the memory allocation of that object 
like in numpy:

Eg. 
import numpy as np 

>>> x = np.arrat([1,2,3])
>>> print(x)
>>> array([1,2,3]) # Not like the customer example above (1) <__main__.Customer object at 0x000001D142D47D60>

This is done bye the __str__() [User friendly but not what developers use] or __repr__() [More used for developers]
'''
#  With __str__() method 
class Customer:
    def __init__(self, name, balance):    
        self.name, self.balance = name, balance
    
    def __str__(self):    
        cust_str = """    
            Customer:      
                name: {name}      
                balance: {balance}    
        """.format(name = self.name,               
                    balance = self.balance)
        return cust_str

Customer_w_str = Customer(name, balance)
print(f" Printing class Customer with __str__() method: \n {Customer_w_str}")

#  With __repr__() method 
class Customer:
    def __init__(self, name, balance):    
        self.name, self.balance = name, balance

    def __repr__(self):
        return "Customer('{name}', {balance})".format(name = self.name, balance = self.balance)

Customer_w_repr = Customer(name, balance)
print(f"Printing with the __repr__() method: \n {repr(Customer_w_repr)}")


'''
For the las part we saw error handling where we can build our custom error handling class if we need to be more specific in our application
'''