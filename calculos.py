def calculateComission(sales, percentage=0.5):
    return sales * percentage


def calculateTotalIncomes(comission, bonus=0):
    return comission + bonus


def calculateTotalSales(sales):
    return sum(sales)


## El parametro bonus se vera afectado por una funcion que determine el bono segun las ventas en el modulo condiciones,
# de manera que sera reasignado en main con el valor determinado y finalmente se sumara en esta funcion
## Comission sera el valor de la primera funcion de este modulo, calculateComission,
# valor el cual se le asignara en el archivo main y finalmente hara su trabajo en la segunda funcion; calculateTotalIncomes
