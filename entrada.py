def readInfo():
    sellerName = input("Ingrese su nombre completo: ")
    sales = float(input("Ingrese sus ventas (C$): "))
    return {
        "sellerName": sellerName,
        "sales": sales
    }


