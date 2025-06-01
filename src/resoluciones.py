def mostrar_saludo():
    print ("Hola Mundo")
pass

def lee_grafo(grafo):
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
    with open(file, 'r', encoding = 'utf-8') as file:
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
    Muestra por pantalla un grafo. El argumento está en formato de lista.
    Formato de entrada: (['A', 'B', 'C'], [('A', 'B'), ('B', 'C')])
    Salida:
    A: B
    B: A, C
    C: B
    '''
    vertices, aristas = grafo
    adyacentes = {v: [] for v in vertices}

    for origen, destino in aristas:
        adyacentes[origen].append(destino)
        adyacentes[destino].append(origen)  # Solo si el grafo es no dirigido

    for vertice in vertices:
        vecinos = ", ".join(adyacentes[vertice])
        print(f"{vertice}: {vecinos}")
pass

def cuenta_grado(grafo_lista):
   
    vertices, aristas = grafo_lista
    grados = {v: 0 for v in vertices}
    
    for origen, destino in aristas:
        grados[origen] += 1
        grados[destino] += 1  # porque es un grafo no dirigido
    
    return grados
pass