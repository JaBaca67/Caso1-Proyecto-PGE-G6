from calculos import calculateComission, calculateTotalIncomes, calculateTotalSales
from condiciones import determineBonus, determinePercentage

def showData(sellerData):
    sellerName = sellerData["sellerName"]
    sales = sellerData["sales"]

    percentage = determinePercentage(sales)
    bonus = determineBonus(sales)
    comission = calculateComission(sales, percentage)
    total = calculateTotalIncomes(comission, bonus )

    sellerData["percentage"] = percentage
    sellerData["bonus"] = bonus
    sellerData["comission"] = comission
    sellerData["totalIncomes"] = total

    print("=== DATOS DEL VENDEDOR ===")
    print(f"Vendedor: {sellerName}")
    print(f"Ventas: {sales}")
    print(f"Porcentaje: {percentage * 100}%")
    print(f"Comisiones: {comission}")
    print(f"Bonus: {bonus}")
    print(f"Total: {total}")

    return sellerData


def showAllData(lista_vendedores):
    print("[Datos de todos los vendedores]")
    
    if len(lista_vendedores) == 0:
        print("Aún no se ha registrado ningún vendedor en el sistema.")
        return # Sale de la función si está vacío

    for i, sellers in enumerate(lista_vendedores, start=1):
        print(f"--- Vendedor #{i} ---")
        print(f"Nombre: {sellers['sellerName']}")
        print(f"Ventas: {sellers['sales']}")
        print(f"Comisiones: {sellers['comission']}")
        print(f"Bonus: {sellers['bonus']}")
        print(f"Ingreso Total: {sellers['totalIncomes']}")
        print("-" * 25)

