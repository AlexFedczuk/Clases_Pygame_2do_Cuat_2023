# Ejercicio -> https://www.pybeselegidos.fun/1-file-city/desafío-1-1
import random
from funciones_validaciones import validar_numero_entero
from funciones_input import pedir_un_numero_entero

opcion_elegida = None
opcion_elegida_final = None
opcion_maquina = None
lista_opciones = ["Vaccine", "Virus", "Data"]
respuesta = None
# MENSAJES
lista_mensajes = ["Gana el usuario!", "Derrota...", "Empate!"]

while True:
    print("\n* VACCINE VS. VIRUS VS. DATA *")
    print("1. Vaccine")
    print("2. Virus")
    print("3. Data")
    print("4. Salir del juego.")
    opcion_elegida = input("Ingrese una de las siguientes opciones: ")
    #opcion_elegida = pedir_un_numero_entero("Ingrese una de las siguientes opciones: ", "ERROR! Debe ingresar un numero.")

    #print(f"\nVALOR INGRESADO {opcion_elegida}, tipo: {type(opcion_elegida)}\n")

    if validar_numero_entero(opcion_elegida):
        opcion_elegida = int(opcion_elegida)
        if opcion_elegida > 0 and opcion_elegida < 5:
            if opcion_elegida == 4:
                break
            opcion_elegida_final = lista_opciones[opcion_elegida - 1]
            opcion_maquina = random.choice(lista_opciones)
        else:
            print("ERROR! El numero ingresado no es una opcion valida.")
    else:
        print("ERROR! Debe ingresar un numero.")

    if opcion_elegida_final != None:
        print(f"La opcion elegida fue {opcion_elegida_final}.")
        print(f"La opcion elegida por la computadora es {opcion_maquina}...")

        match opcion_elegida_final:
            case "Vaccine":
                if opcion_maquina == "Virus":
                    print(lista_mensajes[0])
                elif opcion_maquina == "Data":
                    print(lista_mensajes[1])
                else:
                    print(lista_mensajes[2])
            case "Virus":
                if opcion_maquina == "Data":
                    print(lista_mensajes[0])
                elif opcion_maquina == "Vaccine":
                    print(lista_mensajes[1])
                else:
                    print(lista_mensajes[2])
            case _: # El guion bajo seria el 'Default' del Switch.
                if opcion_maquina == "Vaccine":
                    print(lista_mensajes[0])
                elif opcion_maquina == "Virus":
                    print(lista_mensajes[1])
                else:
                    print(lista_mensajes[2])
        
        respuesta = input("Desea jugar otra vez? Si(s) No(Cualquier tecla): ").lower()
        #print(f"\nRESPUESTA {respuesta}\n")
        if respuesta != "s":
            break