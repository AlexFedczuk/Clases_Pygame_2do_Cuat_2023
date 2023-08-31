from funciones_validaciones import *

def pedir_un_numero_entero(mensaje:str, mensaje_error:str) -> int:
    while True:
        numero_ingresado = input(mensaje)

        if validar_numero_entero(numero_ingresado):
            numero_validado = int(numero_ingresado)
            break
        else:
            print(mensaje_error)

    return numero_validado