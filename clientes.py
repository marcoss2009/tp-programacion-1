def menuIngresoClientes(clientes, saldos):
    # Solicita al usuario que ingrese un legajo
    legajo = int(input("Ingrese un número de cliente: "))
    
    # Si legajo es -1 salimos del modulo
    while legajo != -1:
        # Verifica si el legajo ya existe en la lista de clientes
        while legajo in clientes:
            print("El cliente ya existe. Por favor, ingrese uno diferente.")
            legajo = int(input("Ingrese un número de cliente: "))
        
        # Si el legajo no existe, lo añade a la lista de clientes y el saldo a la lista de saldos
        clientes.append(legajo)
        saldos.append(0)
        print(" Cliente ingresado correctamente ".center(80, '-'))

        # Solicita al usuario que ingrese un legajo
        legajo = int(input("Ingrese un número de cliente: "))

    

def menuConsultaClientes(clientes, saldos, operaciones, vendedores):
    print("3. Consulta de Cliente")
    # Solicita al usuario que ingrese un legajo
    legajo = int(input("Ingrese un número de cliente: "))
    # verificar que el legajo exista
    while legajo not in clientes:
        print("El cliente no existe. Por favor, ingrese uno valido.")
        legajo = int(input("Ingrese un número de cliente: "))
        
    # Buscar indice del legajo
    indice = clientes.index(legajo)
    for i in range(len(operaciones)):
        if operaciones[i][0]== indice:
            print("vendedor:",vendedores[operaciones[i][1]])
            print("codigo de operacion:",operaciones[i][2])
            print("monto de operacion: $",operaciones[i][3])
            if operaciones[i][4]== True:
                print("tipo de operacion:factura")
            else:
                print("tipo de operacion:recibo")
    print("")
    print("saldo final del cliente: $",saldos[indice])