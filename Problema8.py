import scripts.mis_funciones as mis_funciones

def main():
    # Generar la lista de números aleatorios
    lista_aleatoria = mis_funciones.generar_numeros_aleatorios()
    
    # Mostrar la lista obtenida por pantalla
    mis_funciones.mostrar_lista(lista_aleatoria)
    
    # Ordenar los valores de la lista y mostrarla por pantalla
    mis_funciones.ordenar_lista(lista_aleatoria)

if __name__ == "__main__":
    main()
