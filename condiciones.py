def determine_Percentage(sales):
    if sales >= 15000:
        return 0.10
    elif sales >= 10000:
        return 0.08
    elif sales >= 5000:
        return 0.05
    else:
        return 0.03
    
def determine_Bonus(sales):
    if sales >= 20000:
        return 2000
    elif sales >= 15000:
        return 1000
    else:
        return 0
    
