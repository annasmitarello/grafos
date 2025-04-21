from grafos.practica1 import *
from grafos.practica2 import *

def main():
    mostrar_saludo()

    grafo = lee_grafo_stdin(['3', 'A', 'B', 'C', 'A B', 'B C', 'C B'])
    print("Grafo leído:", grafo)

    print("Grados:", cuenta_grado(grafo))
    
if __name__ == '__main__':
    main()
