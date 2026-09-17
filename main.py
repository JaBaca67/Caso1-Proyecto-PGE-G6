from Validaciones import validar_sueldo, validar_ventas

print("=== GESTIÓN DE VENTAS Y COMISIONES ===")

sueldo = validar_sueldo()
ventas = validar_ventas()

print("\n=== RESULTADOS ===")
print("Sueldo:", sueldo)
print("Ventas:", ventas)