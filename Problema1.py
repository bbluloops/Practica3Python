def obtener_porcentaje(fraction):
    try:
        numerator, denominator = map(int, fraction.split('/'))
        if numerator > denominator or denominator == 0:
            raise ValueError("La fracción no es válida.")
        
        percentage = (numerator / denominator) * 100
        rounded_percentage = round(percentage)
        
        if rounded_percentage <= 1:
            return "E"
        elif rounded_percentage >= 99:
            return "F"
        else:
            return f"{rounded_percentage}%"
            
    except ValueError:
        print("Error: Por favor, proporcione una fracción válida (X/Y), donde X e Y son enteros y Y no es 0.")
        return None
    except ZeroDivisionError:
        print("Error: El denominador no puede ser 0. Inténtelo de nuevo.")
        return None

def main():
    while True:
        fraction = input("Ingrese una fracción en formato X/Y: ")
        result = obtener_porcentaje(fraction)
        if result is not None:
            print("Cantidad de combustible en el tanque:", result)
            break

if __name__ == "__main__":
    main()
