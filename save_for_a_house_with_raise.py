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
    mon_check = 0
    
    # initiate months count
    months = 0
    
    # Iterate over if the monthly contributions is still lower than target savings while adding months
    while mon_check < target_saving:
        mon_check += (mon_check * rate) + monthly
        months += 1
        
        # Check after every six months then raise the salary 
        if months % 6 == 0:
            mon_check = (mon_check * sal_raise) + mon_check
    
    # Return no. of months
    return months

print(saving_with_raise())