def readInfo():
    sellerName = input("Ingrese su nombre: ")
    sales = float(input("Ingrese sus ventas: "))
    return {
        "sellerName": sellerName,
        "sales": sales
    }


