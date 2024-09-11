# Imports
import clientes
import vendedores
import operaciones
import login
import menu
    
def main():
    # Listas
    vendedoresLista = ["usuario1", "usuario2", "usuario3", "usuario4"]
    claves = ["1234", "5678", "9012", "3456"]

    clientesLista = []
    saldos = []

    operacionesLista = []
    
    print(" Cathedral Software ".center(80, '-'))
    
    # Ingreso al sistema
    login.menuIngreso()

    # Menú
    opcion = menu.mainMenu()

    while (opcion != 7):
        # Can be a switch?
        if (opcion == 1):
            clientes.menuIngresoClientes()

        if (opcion == 2):
            operaciones.menuOperaciones(operacionesLista, vendedoresLista, clientesLista, saldos)

        if (opcion == 3):
            clientes.menuConsultaClientes()

        if (opcion == 4):
            operaciones.menuMovimientos()

        if (opcion == 5):
            vendedores.menuVendedores(vendedoresLista,operacionesLista,clientesLista)

        if (opcion == 6):
            operaciones.menuCuentasCorrientes()

        opcion = menu.mainMenu()

    print(" Gracias por utilizar Cathedral Software ".center(80, '-'))
    print(" π".rjust(80, '-'))

if __name__ == "__main__":
    main()