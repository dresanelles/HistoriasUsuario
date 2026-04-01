# Funciones

def agregarProducto(inventario):
        nombre = input("Nombre del producto: ")


        precioValido = False

        while precioValido == False:
            try:
                precio = float(input("Precio: "))
                precioValido = True
            except:
                print("Error, ingresa un valor correcto para el precio.")


        cantidadValida = False

        while cantidadValida == False:
            try:
                cantidad = int(input("Cantidad: "))
                cantidadValida = True
            except:
                print("Error, ingresa un valor correcto para la cantidad.")
        
        producto = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }

        inventario.append(producto)

        print("\nProducto agregado correctamente")

def mostrarInventario(inventario):
    if len(inventario) == 0:
         print("El inventario está vacío.")
    else:
        print("\n INVENTARIO: \n")
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

def estadistica(inventario):
    if len(inventario) == 0:
        print("No hay productos para calcular estadisticas.")
    else:
        totalInventario = 0
        totalProductos = 0

        for producto in inventario:
            totalInventario += producto["precio"] * producto["cantidad"]
            totalProductos += producto["cantidad"]

        producto_mas_caro = max(inventario, key=lambda p: p["precio"])    
        producto_mas_stock = max(inventario, key=lambda p: p["cantidad"])


        print(f"\nValor total del inventario: {totalInventario}")
        print(f"Cantidad total de productos: {totalProductos}")

        print(f"Producto más caro: {producto_mas_caro['nombre']} - {producto_mas_caro['precio']}")
        print(f"Producto con más stock: {producto_mas_stock['nombre']} - {producto_mas_stock['cantidad']}")


def buscarProducto(inventario, nombre):

    nombre = nombre.strip().lower()

    for producto in inventario:
        if producto["nombre"].strip().lower() == nombre:
            return producto
    return None

def eliminarProducto(inventario):
    nombre = input("Nombre del producto a eliminar: ")
    producto = buscarProducto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        print("Producto eliminado correctamente!")
    else:
        print("Producto no encontrado.")

def actualizarProducto(inventario):
    nombre = input("Nombre del producto a actualizar: ")
    producto = buscarProducto(inventario, nombre)

    if producto:
        try:
            nuevo_precio = float(input("Nuevo precio: "))
            nueva_cantidad = int(input("Nueva cantidad: "))

            producto["precio"] = nuevo_precio
            producto["cantidad"] = nueva_cantidad

            print("Producto actualizado correctamente")
        except:
            print("Error, datos invalidos")
    
    else:
        print("Producto no encontrado")