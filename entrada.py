def readInfo():
    sellerName = input("Ingrese su nombre: ")
    baseSalary = float(input("Ingrese su sueldo base: "))
    sales = float(input("Ingrese sus ventas: "))
    return {
        "sellerName": sellerName,
        "baseSalary": baseSalary,
        "sales": sales
    }


