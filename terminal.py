# Importamos la librería OS para acceder a funciones del sistema operativo
# Gracias a la segunda parte del proyecto por compartirnos este fragmento de código :)
from os import system, name

def limpiarTerminal():
    # Verifiquemos si estamos en Windows (NT = Windows Kernel)
    if name == "nt":
        system('cls')
    else:
        # Estamos en UNIX, osea todo lo que está bien: mac, linux, etc.
        system('clear')

    print(" Cathedral Software ".center(80, '='))