def showData(sellerData):
    sellerName = sellerData["sellerName"]
    baseSalary = sellerData["baseSalary"]
    sales = sellerData["sales"]

    print("=== DATOS DEL VENDEDOR ===")
    print(f"Vendedor: {sellerName}")
    print(f"Salario base: {baseSalary}")
    print(f"Ventas: {sales}")
