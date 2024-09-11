def menuOperaciones(operaciones, vendedores, clientes, saldos):
    vendedor = input("Ingrese el usuario del vendedor: ")
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

def menuMovimientos():
    print("4. Consulta de Movimientos")

def menuCuentasCorrientes():
    print("6. Consulta de Cuentas Corrientes por Operación")

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