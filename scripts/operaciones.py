def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido en la suma."

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido en la resta."

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido en el producto."

def division(a, b):
    try:
        if b == 0:
            return "Error: No es posible dividir entre cero."
        resultado = a / b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido en la división."

