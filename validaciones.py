#Nota para solo crear rama

#Modulo de Validaciones

def validar_numero(mensaje):
    while True:
        try:
            dato = input(mensaje).strip()

            if dato == "":
                raise ValueError("El dato no puede estar vacio.")
 
            numero = float(dato)

            if numero < 0:
                raise ValueError("El valor no puede ser negativo.")

            return numero

        except ValueError as error:
            print(f"Error: {error}")
            print("Por favor, ingrese un numero valido.")

        finally:
            print("Validacion realizada. ")

def validar_sueldo():
    return validar_numero("Ingrese el sueldo del vendedor:")

def validar_ventas():
    return validar_numero("Ingrese el monto total de ventas: ")