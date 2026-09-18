#Nota para solo crear rama
import  main as main
#Modulo de Validaciones

def validateSales(promptMessage, currentName):
    while True:
        main.clearScreen()
        print("[Módulo de Registro y Cálculo de Comisiones]")
        print(f"Vendedor: {currentName}")
        try:
            
            userInput = input(promptMessage).strip()

            if userInput == "":
                raise ValueError("El dato no puede estar vacío.")

            salesAmount = float(userInput)

            if salesAmount <= 0:
                raise ValueError("El valor de las ventas debe ser mayor a cero.")

            return salesAmount

        except ValueError as error:
            # Captura y traduce el error nativo de Python cuando se ingresan letras en lugar de números
            if "could not convert string to float" in str(error):
                print("Error: El dato ingresado debe ser un valor numérico.")
            else:
                print(f"Error: {error}")
            print("Por favor, ingrese un monto válido.\n")

        finally:
            
            print("[Verificación de entrada de ventas finalizada]")
            input("Presione enter para continuar...")

def validateName(promptMessage):
    
    while True:
        main.clearScreen()
        print("[Módulo de Registro y Cálculo de Comisiones]")
        try:
            userInput = input(promptMessage).strip()

            if userInput == "":
                raise ValueError("El nombre no puede estar vacío.")

            # Verifica que la cadena solo contenga letras (ignorando los espacios)
            nameWithoutSpaces = userInput.replace(" ", "") #Formateamos el nombre para eliminar los espacios y solo validar las letras.
            if nameWithoutSpaces.isalpha() == False: #Actualizamos la validacion para que solo acepte letras y espacios, y no numeros ni caracteres especiales.
                raise ValueError("El nombre no puede contener números ni caracteres especiales.")

            return userInput

        except ValueError as error:
            print(f"Error: {error}")
            print("Por favor, ingrese un nombre válido.\n")

        finally:
            
            print("[Verificación de entrada de nombre finalizada]")
            input("Presione enter para continuar...")

