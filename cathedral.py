# Imports
import clientes
import vendedores
import operaciones
import login
import menu
import terminal
    
def main():
    # Listas
    vendedoresLista = ["usuario1", "usuario2", "usuario3", "usuario4"]
    claves = [1234, 5678, 9012, 3456]

    clientesLista = [1000, 1001, 1002, 1003] # 1000, 1001, 1002, 1003

    consolidados = [
        [-1000, 1000, 1000, 2500],
        [1500, 1400, -900, -1500],
        [-1000, 0, 0, 0],
        [0, 0, -1800, 1800]
    ] # Mátriz

    operacionesCliente = [
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        2,
        3,
        3
    ]

    operacionesVendedor = [
        0,
        1,
        2,
        3,
        0,
        1,
        2,
        3,
        0,
        2,
        3
    ]

    operacionesOperacion = [
        True,
        False,
        False,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        False
    ] # True, False

    operacionesMonto = [
        1000,
        1000,
        1000,
        2500,
        1500,
        1400,
        900,
        1500,
        1000,
        1800,
        1800
    ] # Montos
    
    # Limpiamos la terminal
    terminal.limpiarTerminal()
    
    # Ingreso al sistema
    login.menuIngreso(vendedoresLista, claves)

    # Menú
    opcion = menu.mainMenu()

    while (opcion != 8):
        #if (opcion == 1):
            # Carga de Clientes
            #clientes.menuIngresoClientes(clientesLista, saldos)

        if (opcion == 2):
            # Carga de Operaciones
            operaciones.cargaOperaciones(operacionesCliente, operacionesVendedor, operacionesOperacion, operacionesMonto, vendedoresLista, clientesLista, consolidados)

        #if (opcion == 3):
            # Consulta de Clientes
            #clientes.menuConsultaClientes(clientesLista, saldos, operacionesLista, vendedoresLista)

        if (opcion == 4):
            # Consulta de Movimientos
            operaciones.consultarMovimientos(operacionesCliente, operacionesVendedor, operacionesOperacion, operacionesMonto, vendedoresLista, clientesLista)

        if (opcion == 5):
            # Consulta de Cuentas Corrientes por Cliente
            operaciones.cuentasCorrientesClientes(operacionesCliente, operacionesOperacion, operacionesMonto, clientesLista)

        #if (opcion == 6):
            # Consulta de Saldo de Ventas por Vendedor

        if (opcion == 7):
            # Consulta del Total Operativo
            operaciones.calcularTotalOperativo(consolidados)

        opcion = menu.mainMenu()

    print(" Gracias por utilizar Cathedral Software ".center(80, '-'))
    print(" π".rjust(80, '-'))

if __name__ == "__main__":
    main()