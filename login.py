def menuIngreso(vendedores, claves):
    # print("Ingreso al Sistema")

    vendedor = input("Ingrese su usuario: ")
    # Comprobar que el vendedor existe
    vendedorExiste = comprobarVendedor(vendedor, vendedores)
    while vendedorExiste == False:
        vendedor = input("Ingrese su usuario: ")
        # Comprobar que el vendedor existe
        vendedorExiste = comprobarVendedor(vendedor, vendedores)

    vendedorIndice = vendedores.index(vendedor)

    clave = int(input("Ingrese clave: "))
    claveVendedor = claves(vendedorIndice)
    chequearClave = comprobarClave(clave, claveVendedor)
    while chequearClave == False:
        clave = int(input("Ingrese clave: "))
        chequearClave = comprobarClave(clave, claveVendedor)

def comprobarVendedor(vendedor, vendedores):
    existe = False

    if vendedor in vendedores:
        existe = True

    return existe

def comprobarClave(clave, claveVendedor):
    resultado = False

    if (clave == claveVendedor):
        resultado = True

    return resultado