import terminal

def mainMenu():
    # Limpiamos la terminal
    terminal.limpiarTerminal()
    print(" Seleccione una opción para comenzar ".center(80,'-'))

    # Seleccione una opción
    print("1. Carga de Clientes")
    print("2. Carga de Operaciones")
    print("3. Consulta de Cliente")
    print("4. Consuta de Movimientos")
    print("5. Consulta de Cuentas Corrientes por Cliente")
    print("6. Consulta Saldo de Ventas por Vendedor")
    print("7. Consulta del Total Operativo")
    print("8. Salir del Sistema")

    opcion = int(input("Seleccione una opción: "))

    while (opcion < 1 or opcion > 8):
        opcion = int(input("Seleccione una opción: "))

    return opcion