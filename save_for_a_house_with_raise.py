def saving_with_raise():
    # User inputs
    annual_sal = float(input("Enter your yearly salary: "))
    sal_percent_save = float(input("Enter the percent of your salary to save, as a decimal: "))
    home_cost = float(input("Enter the cost of your dream home: "))
    sal_raise = float(input("Enter the semi-annual raise, as a decimal: "))
    
    # Down payment portion 25% of home cost
    dwn_payment_portion = 0.25
    
    # Annual earn return rate
    return_rate = 0.05
    
    # Target savings (down payment)
    target_saving = home_cost * dwn_payment_portion
    
    # Annual savings:
    yearly = annual_sal * sal_percent_save
    
    # Monthly contribution:
    monthly = yearly / 12
    
    # Monthly rate of return
    rate = return_rate / 12
    
    # Initiate previous month contribution
    total_savings = 0
    
    # initiate months count
    months = 0
    
    # Iterate over if the monthly contributions is still lower than target savings while adding months
    while total_savings < target_saving:
        total_savings += (total_savings * rate) + monthly
        months += 1
        
        # After every six months raise salary according to % increase 
        if months % 6 == 0:
            monthly = monthly * (1 + sal_raise)
    
    # Return no. of months
    return months

print(saving_with_raise())
