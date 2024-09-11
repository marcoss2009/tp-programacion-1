def menuVendedores(vendedores,operaciones):
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
                    
    print(f"Vendedor: {vendedorBuscado}")
    for i in range(len(clienteLista)):
        print(f"Cliente: {cliente[clienteLista[i]]}")
        if operacionesLista[i] == True:
            facturas = facturas + 1
        elif operacionesLista[i] == False:
            recibos = recibos + 1
        print("cantidad de facturas: ",facturas)
        print("cantidad de recibos: ",recibos)
        print(f"Saldo total del cliente: ${saldoLista[i]}")
        print("-" * 30)

    

def validarVendedor(legajos,buscado): #busqueda secuencial
    n=len(legajos)-1
    while n>-1 and legajos[n]!=buscado:
        n=n-1
    return n



