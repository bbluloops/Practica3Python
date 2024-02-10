class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: ${self.precio}, Año: {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos en el catálogo.")

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if productos_filtrados:
            print(f"Productos del año {año}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No hay productos del año {año} en el catálogo.")


# Ejemplo de uso:
catalogo = Catalogo()

producto1 = Producto("Llantas", 100, 2020)
producto2 = Producto("Frenos", 150, 2021)
producto3 = Producto("Aceite", 20, 2019)

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

print("Todos los productos en el catálogo:")
catalogo.mostrar_productos()

print("\nFiltrar productos por año 2020:")
catalogo.filtrar_por_año(2020)
