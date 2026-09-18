from calculos import calculateComission, calculateTotalIncomes, calculateTotalSales
from condiciones import determineBonus, determinePercentage

def showData(sellerData):
    sellerName = sellerData["sellerName"]
    sales = sellerData["sales"]

    percentage = determinePercentage(sales)
    bonus = determineBonus(sales)
    comission = calculateComission(sales, percentage)
    total = calculateTotalIncomes(comission, bonus )

    print("=== DATOS DEL VENDEDOR ===")
    print(f"Vendedor: {sellerName}")
    print(f"Ventas: {sales}")
    print(f"Porcentaje: {percentage}")
    print(f"Comisiones: {comission}")
    print(f"Bonus: {bonus}")
    print(f"Total: {total}")
