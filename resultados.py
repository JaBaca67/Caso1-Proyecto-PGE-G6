from calculos import calculate_Comission, calculate_Total_Incomes, calculate_Total_Sales
from condiciones import determine_Bonus, determine_Percentage

def showData(sellerData):
    sellerName = sellerData["sellerName"]
    sales = sellerData["sales"]

    percentage = determine_Percentage(sales)
    bonus = determine_Bonus(sales)
    comission = calculate_Comission(sales, percentage)
    total = calculate_Total_Incomes(comission, bonus )

    print("=== DATOS DEL VENDEDOR ===")
    print(f"Vendedor: {sellerName}")
    print(f"Ventas: {sales}")
    print(f"Porcentaje: {percentage}")
    print(f"Comisiones: {comission}")
    print(f"Bonus: {bonus}")
    print(f"Total: {total}")
