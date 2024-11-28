def menuIngresoClientes(clientes, consolidados):
    # Solicita al usuario que ingrese un legajo
    legajo = int(input("Ingrese un número de cliente: "))
    
    # Mientras no sea -1, procesar los datos
    while legajo != -1:
        # Verifica si el legajo ya existe en la lista de clientes
        if legajo in clientes:
            print("El cliente ya existe. Por favor, ingrese uno diferente.")
        else:
            # Si el legajo no existe, lo añade a la lista de clientes y el saldo a la lista de saldos
            clientes.append(legajo)
            consolidados.append([0,0,0,0]) #4 vendedores, al cargarlos tienen saldo 0
            print(" Cliente ingresado correctamente ".center(80, '-'))
        
        # Solicita al usuario que ingrese un nuevo legajo
        legajo = int(input("Ingrese un número de cliente: "))



def menuConsultaClientes(consolidados, clientes):
    print("3. Consulta de Cliente")
    
    buscado = int(input("ingrese un numero de cliente: "))
    while buscado not in clientes:
        print("El cliente no existe")
        buscado = int(input("ingrese un numero de cliente: "))
        
    indice = clientes.index(buscado)
    
    resultado = sum(consolidados[indice])
    
    print(f"El saldo final del cliente es ${resultado}")




existeCliente = lambda buscado, clientesLista: clientesLista.index(buscado) if buscado in clientesLista else -1
