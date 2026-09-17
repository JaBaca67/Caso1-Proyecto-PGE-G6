def calculate_Comission(sales, percentage=0.5):
    return sales * percentage


def calculate_Total_Incomes(comission, bonus=0):
    return comission + bonus
 
def calculate_Total_Sales(sales):
    return sum(sales)

## El parametro bonus se vera afectado por una funcion que determine el bono segun las ventas en el modulo condiciones, 
# de manera que sera reasignado en main con el valor determinado y finalmente se sumara en esta funcion
## Comission sera el valor de la primera funcion de este modulo, calculate_Comission, 
# valor el cual se le asignara en el archivo main y finalmente hara su trabajo en la segunda funcion; calculate_Total_Incomes