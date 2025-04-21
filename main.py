import grafos.resoluciones as p1

def main():
    
    p1.mostrar_saludo()

    p1.lee_grafo_stdin(['3', 'A', 'B', 'C', 'A B', 'B C', 'C B'])

    p1.cuenta_grado(['A','B','C'],[('A','B'),('B','C'),('C','B')]) 
    
if __name__ == '__main__':
    
    main()
