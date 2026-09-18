def determinePercentage(sales):
    if sales >= 15000:
        return 0.10
    elif sales >= 10000:
        return 0.08
    elif sales >= 5000:
        return 0.05
    else:
        return 0.03


def determineBonus(sales):
    monthlyGoal = 15000
    bonusAmount = 1000

    if sales >= monthlyGoal:
        return bonusAmount
    return 0  # Cambio en la funcion determine para que solo tengamos una metas mensual.
