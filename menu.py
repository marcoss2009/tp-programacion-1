def mainMenu():
    # Seleccione una opción
    print(" Seleccione una opción para comenzar ".center(80,'-'))
    print("1. Ingreso de Clientes")
    print("2. Ingreso de Operaciones")
    print("3. Consulta de Cliente")
    print("4. Consuta de Movimientos")
    print("5. Consulta de Cuentas Corrientes por Vendedor")
    print("6. Consulta de Cuentas Corrientes por Operación")
    print("7. Salir del Sistema")

    opcion = int(input("Seleccione una opción: "))

    while (opcion < 1 or opcion > 7):
        opcion = int(input("Seleccione una opción: "))

    return opcion