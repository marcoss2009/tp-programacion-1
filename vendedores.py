def menuVendedores(vendedores,consolidados,clientes):
    print("5. Consulta de Cuentas Corrientes por Vendedor")
    vendedorBuscado = input("Ingrese el vendedor que desea buscar: ")
    while vendedorBuscado not in vendedores:
        print("no se encontro el vendedor.")
        vendedorBuscado = input("Ingrese el vendedor que desea buscar correctamente: ")
        
    indice_vendedor = vendedores.index(vendedorBuscado)
    
    
    print(f"Ventas del {vendedorBuscado} con cada cliente:")
    cliente_index = 0
    while cliente_index < len(consolidados):
        cliente_numero = clientes[cliente_index]  # Número real del cliente
        ventas = consolidados[cliente_index][indice_vendedor]
        print(f"Cliente: {cliente_numero} - Saldo final: {ventas}")
        cliente_index += 1


def saldoVendedores(consolidados, vendedores):
    # Consulta de Saldo de Ventas por Vendedor
    buscado = input("ingrese un vendedor: ")
    while buscado not in vendedores:
        print("El vendedor no existe")
        buscado = input("ingrese un vendedor nuevamente: ")
     
    indiceBuscado = vendedores.index(buscado)  
    suma = 0 
    for i in range(len(consolidados)):
        suma = suma + consolidados[i][indiceBuscado]
                
    print(f"el saldo del vendedor {buscado} es: {suma}")
    
            
            




