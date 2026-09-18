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
    print("3. Ver datos de todos los vendedores")
    print("4. Salir del programa")
    #Nota estas opciciones del menu son temporales. Aun se pueden organizar mejor. Más tarde lo hago 😎

    print("═════════════════════════════════════════════════════════════════════")

def systemExecution():

    sellerList = [] #Lista para almacenar los datos de los vendedores.
    option = ""

    #bucle del menú principal
    while option != "4":
        clearScreen()
        showMenu()
        option = input("Selccione una opción (1-4): ").strip()#Selección del menu.
        print()#Espacio en blanco

        if option == "1": 
            clearScreen()
            sellerData = entra.readInfo()

            completeSellerData = resultados.showData(sellerData)

            sellerList.append(completeSellerData)
            #Aun en desarrollo
        
        elif option == "2":
            clearScreen()
            print("[Criterios de comisión y bono]")
            #Aun en desarollo

            #Siguiente prints son temporales, aun puede cambiar a futuro.
            print("• Ventas >= C$20,000   -> C$2,000 de bono")
            print("• Ventas >= C$15,000    -> 10% de comisión + C$1,000 de bono")
            print("• Ventas >= C$10,000 -> 8% de comisión")
            print("• Ventas >= C$5,000    -> 5% de comisión")
            print("• Ventas < C$5,000    -> 3% de comisión")

        elif option == "3":
            clearScreen()
            resultados.showAllData(sellerList)
            #Aun en desarrollo
            

        elif option == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción invalida. Porfavor, ingrese un número del 1 - 4.")

        if option != "4":
            input("Presione enter para volver al menú principal...")
            print("\n" * 2) #Esto sirve para dejar mas espacio desues den input.

if __name__ == "__main__":
    systemExecution()

        
