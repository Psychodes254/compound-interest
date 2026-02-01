class Saver():
    def __init__(self, salary, portion, semi_annual_raise=None):
        self.salary = salary
        self.portion = portion
        self.semi_annual_raise = semi_annual_raise
        
    def monthly_income(self):
        return (self.salary * self.portion) / 12
    
    def apply_raise(self, months):
        for month in range(months):
            if month % 6 == 0:
                return self.monthly_income() * (1 + self.semi_annual_raise)  
         
    
    def __str__(self):
        month_income = f"{self.monthly_income:.2f}"
        applied_raise = f"{self.apply_raise:.2f}"
        
        retstr = f"Monthly Income: ${month_income}"
        retstr += f"Salary with raise: ${applied_raise}"
        
        return retstr
    
    
class SavingsAccount():
    def __init__(self, balance, annual_rate):
        self.balance = balance
        self.annual_rate = annual_rate
        
    def apply_interest(self):
        monthly_rate = self.annual_rate / 12
        
        interest = self.balance * (1 + monthly_rate)
        
        annual_interest = interest - self.balance
        
        return f"Annual Interest: ${annual_interest:.2f}"
    
    def deposit(self, amount):
        pass
    

class Goal():
    def __init__(self, house_cost, down_payment):
        self.house_cost = house_cost
        self.down_payment = down_payment

    def required_amount(self):
        pass
    
    def is_reached(self, balance):
        pass
    
saver = Saver(100000, .25, .1)
savings = SavingsAccount(800000, .05)

print(saver.monthly_income())
print(saver.apply_raise(18))

print(savings.apply_interest())