#! /usr/bin/python

# 1ra Practica Laboratorio 
# Teoria de Grafos
# Consigna: Implementar los siguientes metodos

import sys

def mostrar_saludo():
    print ("Hola Mundo")
pass

def lee_grafo_stdin(grafo):
    cant_vert = int(grafo[0])
    vertices = grafo[1 : 1 + cant_vert]

    aristas = []

    for arista_str in grafo[1 + cant_vert:]:
        nodo1, nodo2 = arista_str.split()
        aristas.append ((nodo1, nodo2))

    return (vertices, aristas)
    
pass

def lee_grafo_archivo(file):
    grafo = []
    with open(file, 'r', enconding = 'utf-8') as file:
        for linea in file:
            grafo.append(linea.strip())
    
    cant_vert = int(grafo[0])
    vertices = grafo[1 : 1 + cant_vert]

    aristas = []

    for arista_str in grafo[1 + cant_vert:]:
    nodo1, nodo2 = arista_str.split()
    aristas.append ((nodo1, nodo2))

    return(vertices, aristas)

pass
    

def imprime_grafo_lista(grafo):
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    pass

#################### FIN EJERCICIO PRACTICA ####################
def lee_entrada_1():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    '''
    data_input = []
    
    for line in sys.stdin:
        if line == '\n':
            break
        else:
            # Con strip() eliminamos los '\n' del final de c/line
            data_input.append(line.strip())
            
    return data_input

    
def lee_entrada_2():
    count = 0
    try:
        while True:
            line = input()
            count = count + 1
            print ('Linea: [{0}]').format(line)
    except EOFError:
        pass
    
    print ('leidas {0} lineas').format(count)
