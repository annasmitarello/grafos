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

def lee_grafo(file):
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

def cuenta_grado(grafo_lista):
   
    vertices, aristas = grafo_lista
    grados = {v: 0 for v in vertices}
    
    for origen, destino in aristas:
        grados[origen] += 1
        grados[destino] += 1  # porque es un grafo no dirigido
    
    return grados
pass