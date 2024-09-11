def menuVendedores(vendedores,operaciones,clientes):
    print("5. Consulta de Cuentas Corrientes por Vendedor")
    vendedorBuscado = input("Ingrese el legajo del vendedor que desea buscar: ")
    indiceValidacion = validarVendedor(vendedores,vendedorBuscado)
    while indiceValidacion == -1:
        vendedorBuscado = input("El vendedor ingresado no existe. Ingrese nuevamente: ")
        indiceValidacion = validarVendedor(vendedores,vendedorBuscado)
        

    clienteLista = []
    operacionesLista = []
    saldoLista = []
    
    #operaciones = [cliente, vendedor, codigo, monto, operacion]
    for operacion in operaciones:
        cliente, vendedor, codigo, monto, tipo_operacion = operacion
        
        if vendedor == indiceValidacion:
            if cliente not in clienteLista:
                clienteLista.append(cliente)
                saldo_inicial = monto if tipo_operacion == True else -monto
                saldoLista.append(saldo_inicial)
                operacionesLista.append([tipo_operacion])
            else:
                # Si el cliente ya está en la lista, actualizamos su saldo y operaciones
                indice_cliente = clienteLista.index(cliente)
                operacionesLista[indice_cliente].append(tipo_operacion)
                
                # Actualizar el saldo según el tipo de operación
                if tipo_operacion == True:
                    saldoLista[indice_cliente] += monto
                elif tipo_operacion == False:
                    saldoLista[indice_cliente] -= monto
                    
    print(f" Cuentas Corrientes del Vendedor: {vendedorBuscado} ".center(80, '-'))
    if len(clienteLista) == 0:
        print(" No hay movimientos para mostrar ".center(80, '-'))
    else:
        for i in range(len(clienteLista)):
            facturas = 0
            recibos = 0
            for j in range(len(operacionesLista[i])):
                if operacionesLista[i][j] == True:
                    facturas = facturas + 1
                elif operacionesLista[i][j] == False:
                    recibos = recibos + 1
                
            print(f"Cliente: {clientes[clienteLista[i]]}")
            print("cantidad de facturas: ",facturas)
            print("cantidad de recibos: ",recibos)
            print(f"Saldo total del cliente: ${saldoLista[i]}")
            print("-" * 30)

    

def validarVendedor(legajos,buscado): #busqueda secuencial
    n=len(legajos)-1
    while n>-1 and legajos[n]!=buscado:
        n=n-1
    return n



