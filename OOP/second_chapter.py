'''
In this chapter we learn what was inheritence, class attributes and how they behave 

The fundamental part from Inheritance is just following the DRY principal where DRY stands for 
    - Don't 
    - Repeat 
    - Yourself 

Wiht this we can build a core class and creating another class that inherits the attributes and functionalities from the parent class 
'''


class BankAccount:
    def __init__(self, firstName, lastName,startingBalance,age ):
        self.firstName = firstName
        self.lastName = lastName
        self.startingBalance = startingBalance
        self.age = age

    def sayHello(self):
        print(f'Thanks for joinng Carte Bank {self.firstName} {self.lastName} your total ${self.startingBalance} it is safe here!!')


class RetirmentAccount(BankAccount):
    def __init__(self,firstName, lastName,startingBalance,age,retireAge):
        super().__init__(firstName, lastName,startingBalance,age)
        #or BankAccount.__init__(self, ..)
        self.retireAge = retireAge
        self.saved_for_retirment = self._saved_for_retirement()
    
    def _saved_for_retirement(self, anual_interest = 0.05):
        total_amount = self.startingBalance * ((1 + anual_interest)**(self.retireAge - self.age))
        return total_amount



c1 = RetirmentAccount('Benito','Carte',500,25,40)
print(f"Mr {c1.firstName + c1.lastName} given the first amount ${c1.startingBalance} after {c1.retireAge - c1.age} years your final amount is {c1.saved_for_retirment}")

