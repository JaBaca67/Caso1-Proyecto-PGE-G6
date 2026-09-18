import validaciones

def readInfo():
    #Se agrego la funcion de validacion de nombre y ventas para que el usuario ingrese los datos del vendedor de manera segura y controlada.
    sellerName = validaciones.validateName("Ingrese el nombre del vendedor: ")
    sales = validaciones.validateSales("Ingrese el monto total de ventas: ", sellerName)  # Pasamos el nombre del vendedor como argumento para mostrarlo en la validación de ventas

# Guardamos los datos validados en el diccionario y los retornamos
    SellerData = {
        "sellerName": sellerName,
        "sales": sales
    }

    return SellerData


