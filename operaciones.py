def menuOperaciones(operaciones, vendedores, clientes, saldos):
    # No permitir la carga de operaciones si no existen clientes
    if (len(clientes) > 0):
        vendedor = input("Ingrese el usuario del vendedor: ")

        # Si vendedor es -1 volvemos al programa principal
        while vendedor != "-1":
            # Comprobar vendedor
            vendedorID = comprobarObtenerVendedor(vendedor, vendedores)
            while vendedorID == -1:
                vendedor = input("Vendedor inexistente. Ingrese el usuario del vendedor: ")
                vendedorID = comprobarObtenerVendedor(vendedor, vendedores)
            
            cliente = int(input("Ingrese el código del cliente: "))
            # Comprobar cliente
            clienteID = comprobarObtenerCliente(cliente, clientes)
            while clienteID == -1:
                cliente = int(input("Cliente inexistente. Ingrese el código del cliente: "))
                clienteID = comprobarObtenerCliente(cliente, clientes)
            
            operacion = int(input("Ingrese 0 si esta operación es un recibo o 1 si es una factura: "))
            while operacion < 0 or operacion > 1:
                operacion = int(input("Ingrese 0 si esta operación es un recibo o 1 si es una factura: "))
            operacion = bool(operacion)

            codigo = int(input("Ingrese el código de la operación: "))
            # Comprobar que el código no esté repetido
            verificarCodigo = comprobarCodigo(codigo, operaciones)
            while verificarCodigo == True:
                codigo = int(input("El código ya existe en otra operación. Ingrese el código de la operación: "))
                verificarCodigo = comprobarCodigo(codigo, operaciones)

            monto = int(input("Ingrese el monto de la operación: "))
            while monto < 1:
                monto = int(input("Ingrese el monto de la operación: "))

            # Sumamos la operación en la matríz
            operaciones.append([clienteID, vendedorID, codigo, monto, operacion])

            # Sumamos o restamos el saldo al cliente
            if (operacion == True):
                # Es una factura, sumamos
                saldos[clienteID] = saldos[clienteID] + monto
            else:
                # Es un recibo, restamos
                saldos[clienteID] = saldos[clienteID] - monto
            print(" Operación cargada correctamente ".center(80, '-'))
            
            # Vuelvo a pedir un vendedor
            vendedor = input("Ingrese el usuario del vendedor: ")
    else:
        print(" Error: Debe cargar al menos un cliente para comenzar a cargar operaciones ".center(80, '-'))

def menuMovimientos(lista, vendedores, clientes):
    print("4. Consulta de Movimientos")
     #len para saber la cantidad de filas que tiene la lista
    i= len(lista)-1
    #para recorrer la lista de forma descendente
    while i !=-1:
        print("cliente: ",clientes[lista[i][0]])
        print("vendedor: ",vendedores[lista[i][1]])
        print("codigo de operacion: ",lista[i][2])
        print("monto de operacion: ",lista[i][3])
        if lista[i][4]== True:
            print("tipo de operación: Factura")
        else:
            print("tipo de operacion: Recibo")
        
        print("-------------------------------")
        i= i-1
            

def menuCuentasCorrientes(lista, vendedores, clientes):
    print("6. Consulta de Cuentas Corrientes por Operación")
    operacion = int(input("Ingrese 0 para transacciones de recibo o 1 para transacciones de factura: "))
    # digitar 1 para pedir factura o 0 para pedir recibo
    while operacion < 0 or operacion > 1:
        operacion = int(input("Ingrese 0 para transacciones de recibo o 1 para transacciones de factura: "))
    operacion = bool(operacion)
    i= len(lista)-1
    #while para recorrer la lista de forma descendente
    while i !=-1:
        #solo muestro las filas que me coinciden con 1 para factura o 0 para recibo
        if lista[i][4]== operacion:
            print("cliente: ",clientes[lista[i][0]])
            print("vendedor: ",vendedores[lista[i][1]])
            print("codigo de operacion: ",lista[i][2])
            print("monto de operacion: ",lista[i][3])
            if lista[i][4]== True:
                print("tipo de operación: Factura")
            else:
                print("tipo de operacion: Recibo")
        
            print("-------------------------------")
        #fila-1
        i= i-1
    
def comprobarObtenerCliente(cliente, clientes):
    indice = -1

    # Comprobamos si el cliente existe y devolvemos su índice
    if cliente in clientes:
        indice = clientes.index(cliente)

    return indice

def comprobarObtenerVendedor(vendedor, vendedores):
    indice = -1

    # Comprobamos si el vendedor existe y devolvemos su índice
    if vendedor in vendedores:
        indice = vendedores.index(vendedor)

    return indice

def comprobarCodigo(codigo, operaciones):
    indice = False

    i = len(operaciones) - 1

    while i != -1:
        if codigo in operaciones[i]:
            # Existe en este índice, terminamos el recorrido
            i = -1
            indice = True
        else:
            # No existe en este índice, sigamos recorriendo la matríz
            i = i - 1

    return indice