
inventario = []

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
            
        print(f"\nValor total del inventario: {totalInventario}")
        print(f"Cantidad total de productos: {totalProductos}")

salir = False

#Bucle Principal

while salir == False:


    #Menu Principal

    print("\n------- SISTEMA DE INVENTARIO ------\n")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadisticas")
    print("4. Salir")

    # Validar opcion escogida

    seleccionValida = False

    while seleccionValida == False:

        try:
            seleccion = int(input("\nElige una opción: "))
            seleccionValida = True
            
        except ValueError:
            print("Error, Ingresa una opción valida")

    # Agregar Producto

    if seleccion == 1:
        agregarProducto(inventario)

    # Mostrar inventario

    elif seleccion == 2:
        mostrarInventario(inventario)
        
    # Estadisticas

    elif seleccion == 3:
        estadistica(inventario)     

    # Saliendo del bucle  
    
    elif seleccion == 4:
        print("Saliendo...\n")
        salir = True
    
    else:
        print("\nError, intenta de nuevo")






""" Este programa permite gestionar un inventario mediante un menú interactivo.
El usuario puede agregar productos, visualizarlos y calcular estadísticas.
Se utilizan listas y diccionarios para almacenar la información,
junto con estructuras de control como bucles y condicionales. """