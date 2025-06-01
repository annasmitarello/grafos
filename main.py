import src.resoluciones as p1

def main():
    # Muestra un saludo
    p1.mostrar_saludo()

    # Grafo de ejemplo (entrada como lista de strings tipo stdin)
    entrada = ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']

    # Leer grafo desde entrada
    grafo = p1.lee_grafo(entrada)

    # Mostrar lista de adyacencias
    print("\n=== Lista de adyacencias ===")
    p1.imprime_grafo_lista(grafo)

    # Calcular y mostrar grados
    print("\n=== Grado de cada vértice ===")
    grados = p1.cuenta_grado(grafo)
    for v, g in grados.items():
        print(f"{v}: {g}")

    # Vértices aislados
    print("\n=== Vértices aislados ===")
    aislados = p1.vertice_aislado(grafo)
    print(aislados)

    # Componentes conexas
    print("\n=== Componentes conexas ===")
    componentes = p1.componentes_conexas(grafo)
    for i, comp in enumerate(componentes, 1):
        print(f"Componente {i}: {comp}")

    # ¿Es conexo?
    print("\n=== ¿Es conexo? ===")
    print(p1.es_conexo(grafo))

if __name__ == '__main__':
    main()
