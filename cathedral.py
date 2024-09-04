def main():
    # Imports
    import clientes
    import vendedores
    import operaciones
    import login

    vendedores = []
    clientes = []
    operaciones = []

    print(" Cathedral Software ".center(80,'-'))
    
    # Ingreso al sistema
    login.menuIngreso()

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

    # Can be a switch?
    if (opcion == 1):
        clientes.menuIngresoClientes()

    if (opcion == 2):
        operaciones.menuOperaciones()

    if (opcion == 3):
        clientes.menuConsultaClientes()

    if (opcion == 4):
        operaciones.menuMovimientos()

    if (opcion == 5):
        vendedores.menuVendedores()

    if (opcion == 6):
        operaciones.menuCuentasCorrientes()
        
if __name__ == "__main__":
    main()