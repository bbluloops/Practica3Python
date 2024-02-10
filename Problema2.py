def main():
    while True:
        try:
            calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")

            calificaciones_lista = calificaciones_str.split(',')
            
            calificaciones_entero = [int(calificacion.strip()) for calificacion in calificaciones_lista]
            
            print("Calificaciones convertidas a enteros:", calificaciones_entero)
            break  
        except ValueError:
            print("Error: Se esperaban valores numéricos.")
        except Exception as e:
            print("Error inesperado:", e)

if __name__ == "__main__":
    main()
