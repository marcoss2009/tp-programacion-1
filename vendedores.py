import terminal

def saldoVendedores(consolidados, vendedores):
    # Limpiamos la terminal
    terminal.limpiarTerminal()

    print(" Consulta Saldo de Ventas por Vendedor ".center(80,'-'))

    # Consulta de Saldo de Ventas por Vendedor
    buscado = input("Ingrese un vendedor: ")
    while buscado not in vendedores:
        print("El vendedor no existe")
        buscado = input("Ingrese un vendedor nuevamente: ")
     
    indiceBuscado = vendedores.index(buscado)  
    suma = 0 
    for i in range(len(consolidados)):
        suma = suma + consolidados[i][indiceBuscado]
                
    print(f"El saldo del vendedor {buscado} es: ${suma}")
    input("Presione Enter para continuar...")
    
# Función de Seba, la borró sin querer y no me dí cuenta cuando aprobé el PR
def validarVendedor(legajos,buscado): #busqueda secuencial
    n=len(legajos)-1
    while n>-1 and legajos[n]!=buscado:
        n=n-1
    return n