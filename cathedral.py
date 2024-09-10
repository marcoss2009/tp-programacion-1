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

    clientesLista = [1000,1001,1002,1003,1004]
    saldos = [0,0,0,0,0]

    operacionesLista = [[0,0,3455,100000,True],[1,0,3456,200000,True],[0,0,3457,50000,True],[0,1,2480,150000,False],[2,3,3458,20000,True],[4,1,3459,100000,True],[4,1,2481,25000,False],[1,0,2482,50000,False]]
    
    print(" Cathedral Software ".center(80, '-'))
    
    # Ingreso al sistema
    login.menuIngreso()

    # Menú
    opcion = menu.mainMenu()

    while (opcion != 7):
        # Can be a switch?
        if (opcion == 1):
            clientes.menuIngresoClientes(clientesLista, saldos)

        if (opcion == 2):
            operaciones.menuOperaciones(operacionesLista, vendedoresLista, clientesLista, saldos)

        if (opcion == 3):
            clientes.menuConsultaClientes(clientesLista, saldos, operacionesLista, vendedoresLista)

        if (opcion == 4):
            operaciones.menuMovimientos(operacionesLista,vendedoresLista, clientesLista)

        if (opcion == 5):
            vendedores.menuVendedores()

        if (opcion == 6):
            operaciones.menuCuentasCorrientes(operacionesLista,vendedoresLista, clientesLista)

        opcion = menu.mainMenu()

    print(" Gracias por utilizar Cathedral Software ".center(80, '-'))
    print(" π".rjust(80, '-'))

if __name__ == "__main__":
    main()