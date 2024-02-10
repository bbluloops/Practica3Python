import scripts.operaciones as operaciones

def main():
    a = 10
    b = 5

    print("Suma:", operaciones.suma(a, b))
    print("Resta:", operaciones.resta(a, b))
    print("Producto:", operaciones.producto(a, b))
    print("División:", operaciones.division(a, b))

if __name__ == "__main__":
    main()
