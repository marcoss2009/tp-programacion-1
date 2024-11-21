from vendedores import validarVendedor
from clientes import existeCliente
from tablas import crearTabla
import terminal

def cargaOperaciones(operacionesCliente, operacionesVendedor, operacionesOperacion, operacionesMonto, vendedoresLista, clientesLista, consolidados):
    # Limpiamos la terminal
    terminal.limpiarTerminal()

    print(" Carga de Operaciones ".center(80,'-'))

    # No permitir la carga de operaciones si no existen clientes
    if (len(clientesLista) > 0):
        vendedor = input("Ingrese el usuario del vendedor: ")

        # Comprobar vendedor
        vendedorID = validarVendedor(vendedoresLista, vendedor)
        while vendedorID == -1:
            vendedor = input("Vendedor inexistente. Ingrese el usuario del vendedor: ")
            vendedorID = validarVendedor(vendedoresLista, vendedor)
        
        cliente = int(input("Ingrese el código del cliente: "))
        # Comprobar cliente
        clienteID = existeCliente(clientesLista, cliente)
        while clienteID == -1:
            cliente = int(input("Cliente inexistente. Ingrese el código del cliente: "))
            clienteID = existeCliente(clientesLista, cliente)
        
        operacion = int(input("Ingrese 0 si esta operación es un recibo o 1 si es una factura: "))
        while operacion < 0 or operacion > 1:
            operacion = int(input("Ingrese 0 si esta operación es un recibo o 1 si es una factura: "))
        operacion = bool(operacion)

        monto = int(input("Ingrese el monto de la operación: "))
        while monto <= 0:
            monto = int(input("Ingrese el monto de la operación: "))

        # Guardamos la operación
        operacionesCliente.append(clienteID)
        operacionesVendedor.append(vendedorID)
        operacionesOperacion.append(operacion)
        operacionesMonto.append(monto)

        # Actualizamos el saldo
        # Si es factura restamos, si es recibo sumamos
        if operacion == True:
            consolidados[clienteID][vendedorID] = consolidados[clienteID][vendedorID] - monto
        else:
            consolidados[clienteID][vendedorID] = consolidados[clienteID][vendedorID] + monto

        print(" Operación cargada correctamente ".center(80, '-'))
    else:
        print(" Error: Debe cargar al menos un cliente para comenzar a cargar operaciones ".center(80, '-'))
    
    input("Presione Enter para continuar...")

def cuentasCorrientesClientes(operacionesCliente, operacionesOperacion, operacionesMonto, clientesLista):
    # Limpiamos la terminal
    terminal.limpiarTerminal()

    print(" Cuentas Corrientes por Clientes ".center(80,'-'))

    # Si la lista de operaciones está vacía entoncés qué vamos a leer?
    if (len(operacionesOperacion) > 0):

        cliente = int(input("Ingrese el código del cliente: "))

        # Comprobar cliente
        clienteID = existeCliente(clientesLista, cliente)
        while clienteID == -1:
            cliente = int(input("Cliente inexistente. Ingrese el código del cliente: "))
            clienteID = existeCliente(clientesLista, cliente)

        # Inicializamos las listas para imprimir la tabla
        filas = []
        columnas = ["Movimiento", "Debe", "Haber"] # Debe = Factura; Haber = Recibo

        # Totales
        debe = 0
        haber = 0

        '''''
        Vamos a recorrer la lista de clientes

        Si en algún momento algún registro nos coincide con el ID del cliente buscado
        buscamos el resto de los paramétros de la operación en las otras listas. Al ser listas hermanadas
        entoncés podemos utilizar el mismo índice.
        '''''
        for i in range(len(operacionesCliente)):
            if operacionesCliente[i] == clienteID:
                filas.append([("Factura" if operacionesOperacion[i] == True else "Recibo"), ("$" + str(operacionesMonto[i]) if operacionesOperacion[i] == True else ""), ("" if operacionesOperacion[i] == True else "$" + str(operacionesMonto[i]))])
        
            # Sumamos Debe o Haber
            if operacionesOperacion[i] == True:
                # Es una Factura, sumamos en Debe
                debe = debe + operacionesMonto[i]
            else:
                # Es un Recibo, sumamos en Haner
                haber = haber + operacionesMonto[i]

        # Sumamos como última fila al total de debe y haber
        filas.append(["Suma de Movimientos", "$" + str(debe), "$" + str(haber)])
        filas.append(["", "Saldo Final: ", "$" + str(haber-debe)])

        # Creamos la Tabla
        crearTabla(columnas, filas)
    else:
        print(" Error: Debe cargar al menos una operación para visualizar Cuentas Corrientes ".center(80, '-'))
    
    input("Presione Enter para continuar...")

def calcularTotalOperativo(consolidados):
    # Limpiamos la terminal
    terminal.limpiarTerminal()

    print(" Total Operativo ".center(80,'-'))

    # Si la matríz está vacía entoncés qué vamos a leer?
    if (len(consolidados) > 0):
        total = 0

        # Recorremos toda la matríz
        for i in range(len(consolidados)): # Cliente
            for k in range(len(consolidados[i])): # Vendedor
                total = total + consolidados[i][k]

        # Definimos columna y fila para visualizar la tabla
        columnas = ["Total Operativo"]
        filas = [["$" + str(total)]]

        # Creamos la Tabla
        crearTabla(columnas, filas)
    else:
        print(" Error: Debe cargar al menos una operación para visualizar el Total Operativo ".center(80, '-'))
    
    input("Presione Enter para continuar...")

def consultarMovimientos(operacionesCliente, operacionesVendedor, operacionesOperacion, operacionesMonto, vendedoresLista, clientesLista):
    # Limpiamos la terminal
    terminal.limpiarTerminal()

    print(" Consulta de Movimientos ".center(80,'-'))

    # Hay operaciones para mostrar?
    if (len(operacionesCliente) > 0):
        filtro = int(input("Ingrese 0 para filtrar por recibos, 1 para filtrar por facturas o 2 para mostrar todos los movimientos: "))
        while filtro < 0 or filtro > 2:
            filtro = int(input("Ingrese 0 para filtrar por recibos, 1 para filtrar por facturas o 2 para mostrar todos los movimientos: "))

        columnas = ["Tipo de Movimiento", "Cliente", "Vendedor", "Monto"]
        filas = []

        # Recorremos
        for i in range(len(operacionesCliente)):
            if (filtro == 0 and operacionesOperacion[i] == False):
                filas.append(["Recibo", clientesLista[operacionesCliente[i]], vendedoresLista[operacionesVendedor[i]], "$" + str(operacionesMonto[i])])
            elif (filtro == 1 and operacionesOperacion[i] == True):
                filas.append(["Factura", clientesLista[operacionesCliente[i]], vendedoresLista[operacionesVendedor[i]], "$" + str(operacionesMonto[i])])
            elif (filtro == 2):
                filas.append([("Factura" if operacionesOperacion[i] == True else "Recibo"), clientesLista[operacionesCliente[i]], vendedoresLista[operacionesVendedor[i]], "$" + str(operacionesMonto[i])])

        crearTabla(columnas, filas)
    else:
        print(" Error: Debe cargar al menos una operación para visualizar el Total Operativo ".center(80, '-'))
    
    input("Presione Enter para continuar...")