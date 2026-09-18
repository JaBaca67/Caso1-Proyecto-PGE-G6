#Nota para solo crear rama

#Modulo de Validaciones

def validateSales(promptMessage):
    while True:
        try:
            userInput = input(promptMessage).strip()

            if userInput == "":
                raise ValueError("El dato no puede estar vacío.")

            salesAmount = float(userInput)

            if salesAmount < 0:
                raise ValueError("El valor de las ventas no puede ser negativo.")

            return salesAmount

        except ValueError as error:
            # Captura y traduce el error nativo de Python cuando se ingresan letras en lugar de números
            if "could not convert string to float" in str(error):
                print("Error: El dato ingresado debe ser un valor numérico.")
            else:
                print(f"Error: {error}")
            print("Por favor, ingrese un monto válido.\n")

def validateName(promptMessage):
    while True:
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

