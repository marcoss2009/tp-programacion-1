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

    clientesLista = []
    consolidados = []

    operacionesCliente = []
    operacionesVendedor = []
    operacionesOperacion = []
    operacionesMonto = []
    
    # Limpiamos la terminal
    terminal.limpiarTerminal()
    
    # Ingreso al sistema
    login.menuIngreso(vendedoresLista, claves)

    # Menú
    opcion = menu.mainMenu()

    while (opcion != 8):
        if (opcion == 1):
            # Carga de Clientes
            clientes.menuIngresoClientes(clientesLista, consolidados)

        if (opcion == 2):
            # Carga de Operaciones
            operaciones.cargaOperaciones(operacionesCliente, operacionesVendedor, operacionesOperacion, operacionesMonto, vendedoresLista, clientesLista, consolidados)

        if (opcion == 3):
            # Consulta de Clientes
            clientes.menuConsultaClientes(consolidados, clientesLista)

        if (opcion == 4):
            # Consulta de Movimientos
            operaciones.consultarMovimientos(operacionesCliente, operacionesVendedor, operacionesOperacion, operacionesMonto, vendedoresLista, clientesLista)

        if (opcion == 5):
            # Consulta de Cuentas Corrientes por Cliente
            operaciones.cuentasCorrientesClientes(operacionesCliente, operacionesOperacion, operacionesMonto, clientesLista)

        if (opcion == 6):
            # Consulta de Saldo de Ventas por Vendedor
            vendedores.saldoVendedores(consolidados, vendedoresLista)

        if (opcion == 7):
            # Consulta del Total Operativo
            operaciones.calcularTotalOperativo(consolidados)

        opcion = menu.mainMenu()

    print(" Gracias por utilizar Cathedral Software ".center(80, '-'))
    print(" π".rjust(80, '-'))

if __name__ == "__main__":
    main()