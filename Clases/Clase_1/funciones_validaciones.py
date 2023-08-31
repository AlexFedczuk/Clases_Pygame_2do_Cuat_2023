import re

def validar_numero_entero(cadena:str) -> bool:
    """
    Valida si el string ingresado por parametro representa un numero entero.

    :param parametro1: La cadena ingresada por parametros.
    :return: Devuelve True si es un numero entero el string, un False si no lo es.
    """
    retorno = False
    patron = r"^-?\d+$"
    """
     El patrón verifica si la cadena comienza opcionalmente con un signo "-",
    seguido de uno o más dígitos, y no contiene ningún otro carácter antes
    o después del número. Si la cadena coincide con este patrón, se
    considera un número entero válido.
    """
    if re.match(patron, cadena):
        retorno = True
        
    return retorno

def validar_numero_flotante(cadena:str) -> bool:
    """
    Valida si el string ingresado por parametro representa un numero flotante.

    :param parametro1: La cadena ingresada por parametros.
    :return: Devuelve True si es un numero entero el string, un False si no lo es.
    """
    retorno = False
    patron = r"^-?\d+(\.\d+)?$"
    """
     El patrón verifica si la cadena comienza opcionalmente con un signo "-",
    seguido de uno o más dígitos, y no contiene ningún otro carácter antes
    o después del número. Si la cadena coincide con este patrón, se
    considera un número entero válido.
    """
    if re.match(patron, cadena):
        retorno = True

    return retorno

def validar_cadena_alfabetica(cadena:str) -> bool:
    """
    Valida si el string ingresado por parametro representa caracteres del alfabeto.

    :param parametro1: La cadena ingresada por parametros.
    :return: Devuelve True si todos los caractres del alfabeto complementan la cadena, un False si no lo es.
    """
    retorno = False
    patron = r'^[a-zA-Z]+$'
    """
      Con esta expresion regular estamos verificando que desde el principio hasta el final de la cadena
     se valide que solamente haya caracteres del abcedario en minuscula y mayuscula.
    """
    if re.match(patron, cadena):
        retorno = True

    return retorno

