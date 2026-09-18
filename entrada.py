import validaciones

def readInfo():
    sellerName = validaciones.validateName("Ingrese el nombre del vendedor: ")
    sales = validaciones.validateSales("Ingrese el monto total de ventas: ")

    SellerData = {
        "sellerName": sellerName,
        "sales": sales
    }

    return SellerData


