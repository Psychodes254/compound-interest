def saving_for_a_house():
    y_sal = float(input("Enter your yearly salary: "))
    saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    home_cost = float(input("Enter the cost of your dream home: "))
    dwn_portion = 0.25
    return_rate = 0.05
    
    # Target savings (down payment)
    target_saving = home_cost * dwn_portion
    
    # Monthly savings contribution
    # Annual savings:
    yearly = y_sal * saved
    
    # Monthly contribution:
    monthly = yearly / 12
    
    # Monthly rate of return
    rate = return_rate / 12
    
    # Initiate previous month contribution
    mon_check = 0
    
    # initiate months count
    months = 0
    
    while mon_check < target_saving:
        mon_check += (mon_check * rate) + monthly
        months += 1
    
    # Return no. of months
    return months
    
print(saving_for_a_house())

