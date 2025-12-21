def choosing_interest_rate():
    # User input, their first deposit
    initial_deposit = float(input("Enter the initial deposit: "))
    
    # Constant home cost
    house_cost = 800000
    
    # Down payment constant percentage
    down_payment = house_cost * .25
    
    # 3 years needed for maximum time needed to reach down payment goal
    req_months = 36
    
    # Initiate the lower bound
    lower_bound = 0.0

    # Initiate the upper bound
    upper_bound = 1.0
    
    # Savings should be within $100 since hitting exact figure is challenging
    epsilon = 100
    
    # Initiate the steps that will take to accomplish the bisection search
    steps = 0
    
    # Initial guess
    rate = (upper_bound + lower_bound) / 2
    
    # First check if it is possible to reach the goal with 100% interest
    if initial_deposit * (1 + upper_bound / 12) ** req_months < down_payment:
        print("It is not possible to reach the savings goal in 3 years with a 100% interest rate.")
        return

    # Start the while loop if the goal is possible 
    while True:
        steps += 1
        
        monthly_rate = rate / 12
        
        # Use the compound interest formula
        amount_saved = initial_deposit * (1 + monthly_rate) ** req_months
        
        # If the difference between the amount saved and the down payment 
        # is lower or equal to epsilon, goal reached, the loop must be broken
        if abs(amount_saved - down_payment) <= epsilon:
            break
        
        # If we saved too much, then the rate is high
        if amount_saved > down_payment:
            upper_bound = rate
        # If we saved too litte, then the rate is low
        else:
            lower_bound = rate
        
        # Recalculate the guess
        rate = (upper_bound + lower_bound) / 2
        
        # Safely break the loop if steps exceeds 100
        if steps >= 100:
            break
        
    print("Best savings rate: ", rate)
    
    print("Steps in bisection search: ", steps)
    
    return rate

required_rate = choosing_interest_rate()

print(f"Minimum annual rate of return: {required_rate:.4f} (or {required_rate*100:.2f}%)")
