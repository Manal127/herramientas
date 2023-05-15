import random
import pide_num

def pintar_lista(lista):
    for elementos in lista:
        numero_posicion = lista.index(elementos)
        print(f"{numero_posicion} <😀> {elementos}")

def elige_valor(lista):
    pintar_lista(lista)
    indice_usuario = -1
    while indice_usuario not in range(len(lista)):
        print(f"introduce un número entre 0 y {len(lista)-1}")
        indice_usuario = pide_num.pideUnNum()
    valor_lista = lista[indice_usuario]
    
    return valor_lista

def valor_aleatorio(lista):
    posiciones = len(lista)
    aleatorio =random.randrange(posiciones)
    
    return lista[aleatorio]

def indice_aleatorio(lista):
    posiciones = len(lista)
    aleatorio = random.randrange(posiciones)

    return aleatorio