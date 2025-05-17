
def agregar_producto(nombres, cantidades):
    """
    Agrega un nuevo producto al stock.

    Args:
        nombres (list): Lista de nombres de productos.
        cantidades (list): Lista de cantidades de productos.
    """
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad >= 0:
                break
            else:
                print("La cantidad debe ser un número entero no negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
    nombres.append(nombre)
    cantidades.append(cantidad)
    print("Producto agregado con éxito.")

def ver_productos_agotados(nombres, cantidades):
    """
    Muestra los productos con stock agotado.

    Args:
        nombres (list): Lista de nombres de productos.
        cantidades (list): Lista de cantidades de productos.
    """
    print("\nProductos agotados:")
    agotados = False
    for i in range(len(nombres)):
        if cantidades[i] == 0:
            print(nombres[i])
            agotados = True
    if not agotados:
        print("No hay productos agotados.")

def actualizar_stock(nombres, cantidades):
    """
    Actualiza el stock de un producto existente.

    Args:
        nombres (list): Lista de nombres de productos.
        cantidades (list): Lista de cantidades de productos.
    """
    producto = input("Ingrese el nombre del producto a actualizar: ")
    if producto in nombres:
        index = nombres.index(producto)
        while True:
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
                if nueva_cantidad >= 0:
                    break
                else:
                    print("La cantidad debe ser un número entero no negativo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
        cantidades[index] = nueva_cantidad
        print("Stock actualizado.")
    else:
        print("Producto no encontrado.")

def ver_todos_los_productos(nombres, cantidades):
    """
    Muestra el listado completo de productos con su stock.

    Args:
        nombres (list): Lista de nombres de productos.
        cantidades (list): Lista de cantidades de productos.
    """
    print("\nListado de productos:")
    if not nombres:  # Verifica si la lista de nombres está vacía
        print("No hay productos registrados.")
        return
    for i in range(len(nombres)):
        print(f"{nombres[i]}: {cantidades[i]}")

def main():
    """
    Función principal del programa.
    """
    nombres = []
    cantidades = []
    salir = False

    while not salir:
        print("\n--- Menú de opciones ---")
        print("1. Agregar producto")
        print("2. Ver productos agotados")
        print("3. Actualizar stock")
        print("4. Ver todos los productos")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            agregar_producto(nombres, cantidades)
        elif opcion == "2":
            ver_productos_agotados(nombres, cantidades)
        elif opcion == "3":
            actualizar_stock(nombres, cantidades)
        elif opcion == "4":
            ver_todos_los_productos(nombres, cantidades)
        elif opcion == "5":
            print("Gracias por usar el sistema.")
            salir = True
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()

