import terminal

def menuIngresoClientes(clientes, consolidados):
    # Limpiamos la terminal
    terminal.limpiarTerminal()

    print(" Carga de Clientes ".center(80,'-'))

    # Solicita al usuario que ingrese un legajo
    legajo = int(input("Ingrese un número de cliente o -1 para volver al menú: "))
    
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
        legajo = int(input("Ingrese un número de cliente o -1 para volver al menú: "))



def menuConsultaClientes(consolidados, clientes):
    # Limpiamos la terminal
    terminal.limpiarTerminal()

    print(" Consulta de Cliente ".center(80,'-'))
    
    # Si la lista de clientes está vacía entonces no podemos buscar nada
    if (len(clientes) > 0):
        buscado = int(input("Ingrese un número de cliente: "))
        while buscado not in clientes:
            print("El cliente no existe")
            buscado = int(input("Ingrese un número de cliente: "))
            
        indice = clientes.index(buscado)
        
        resultado = sum(consolidados[indice])
        
        print(f"El saldo final del cliente es ${resultado}")
    else:
        print(" Error: No hay clientes cargados para consultar ".center(80, '-'))
    
    input("Presione Enter para continuar...")

existeCliente = lambda buscado, clientesLista: clientesLista.index(buscado) if buscado in clientesLista else -1
