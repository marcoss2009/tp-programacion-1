# Imports
import clientes
import vendedores
import operaciones
import login
import menu
    
def main():
    # Listas
    vendedoresLista = []
    claves = []

    clientesLista = []

    operacionesLista = []
    
    print(" Cathedral Software ".center(80,'-'))
    
    # Ingreso al sistema
    login.menuIngreso()

    # Menú
    opcion = menu.mainMenu()

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
        vendedores.menuVendedores(vendedoresLista,operacionesLista)

    if (opcion == 6):
        operaciones.menuCuentasCorrientes()

if __name__ == "__main__":
    main()