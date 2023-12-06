"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, bonus, details):
        self.name = name
        self.contract = contract
        self.bonus = bonus
        self.details = details

    def get_pay(self):
        return self.contract + self.bonus

    def __str__(self):
        return self.details

class Contract:
    def __init__(self, pay, hours):
        self.pay = pay
        self.hours = hours

    def get(self):
        if(self.hours<=1):
            return self.pay
        else:
            return self.pay * self.hours
        
class Bonus:
    def __init__(self, pay, contracts):
        self.pay = pay
        self.contracts = contracts
    
    def get(self):
        if(self.contracts<=1):
            return self.pay
        else:
            return self.pay * self.contracts


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Contract(4000, 0).get(), 0, "Billie works on a monthly salary of 4000. Their total pay is 4000.")

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Contract(25, 100).get(), 0, "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.")

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Contract(3000, 0).get(), Bonus(200, 4).get(), "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.")

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Contract(25, 150).get(), Bonus(220, 3).get(), "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.")

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Contract(2000, 0).get(), Bonus(1500, 0).get(), "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.")

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Contract(30, 120).get(), Bonus(600, 0).get(), "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.")
