#Main donde ocurre y trabajan todos los modulos.
import calculos as cal
import condiciones
import entrada as entra
import resultados
import validaciones
import os #Para crear una función para hacer clear de la consola. Uso universal.

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def showMenu():
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║               SISTEMA DE GESTIÓN DE VENTAS Y COMISIONES              ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")

    print("1. Registrar y calcular comisiones de vendedor")
    print("2. Ver criterios de comisión y metas de bono")
    print("3. Salir del programa")
    #Nota estas opciciones del menu son temporales. Aun se pueden organizar mejor. Más tarde lo hago 😎

    print("═════════════════════════════════════════════════════════════════════")

def systemExecution():

    option = ""

    #bucle del menú principal
    while option != 3:
        clearScreen()
        showMenu()
        option = input("Selccione una opción (1-3): ").strip()#Selección del menu.
        print()#Espacio en blanco

        if option == "1": 
            clearScreen()
            print("[Módulo de Registro y Cálculo de Comisiones]")
            sellerData = entra.readInfo()
            sellerName = sellerData["sellerName"]
            sales = sellerData["sales"]

            calculate_Comission = cal.calculateComission(sellerData["sales"], condiciones.determinePercentage(sellerData["sales"]))
            calculate_Total_Incomes = cal.calculateTotalIncomes(calculate_Comission, condiciones.determineBonus(sellerData["sales"]))

            resultados.showData(sellerData)
            

            #Aun en desarrollo
        
        elif option == "2":
            clearScreen()
            print("[Criterios de comisión y bono]")
            #Aun en desarollo

            #Siguiente prints son temporales, aun puede cambiar a futuro.
            print("• Ventas < $5,000      -> 5% de comisión")
            print("• Ventas $5,000-$9,999 -> 10% de comisión")
            print("• Ventas >= $10,000    -> 15% de comisión + Bono adicional\n")

        elif option == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción invalida. Porfavor, ingrese un número del 1 - 3.")

        if option != "3":
            input("Presione enter para volver al menú principal...")
            print("\n" * 2) #Esto sirve para dejar mas espacio desues den input.

if __name__ == "__main__":
    systemExecution()

        
