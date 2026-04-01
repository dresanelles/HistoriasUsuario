#Semana 3

# print("ESTOY EJECUTANDO ESTE ARCHIVO")
# import os
# print("RUTA REAL:", os.path.abspath(__file__))

from servicios import *
from archivos import *

inventario = []

salir = False

#Bucle Principal

while salir == False:


    #Menu Principal

    print("\n------- SISTEMA DE INVENTARIO ------\n")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadisticas")
    print("4. Buscar producto")
    print("5. Eliminar producto")
    print("6. Actualizar producto")
    print("7. Guardar inventario")
    print("8. Cargar inventario")
    print("9. Salir")

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


    # Buscar producto

    elif seleccion == 4:
        nombre = input("Nombre a buscar: ") 
        producto = buscarProducto(inventario, nombre)

        if producto:
            print(producto)
        else:
            print("No encntrado")

    # Eliminar producto

    elif seleccion == 5:

        eliminarProducto(inventario)


    # Actualizar producto

    elif seleccion == 6:
        actualizarProducto(inventario)

    # Guardar inventario

    elif seleccion == 7:
        guardarJson(inventario)

    
    # Cargar inventario

    elif seleccion == 8:
        nuevo_inventario = cargarJson()

        opcion = input("¿Sobrescribir inventario? (S/N): ").lower()

        if opcion == "s":
            inventario = nuevo_inventario
            print("Inventario sobrescrito correctamente")

        elif opcion == "n":
            for producto_nuevo in nuevo_inventario:
                producto_existente = buscarProducto(inventario, producto_nuevo["nombre"])

                if producto_existente:
                    producto_existente["cantidad"] += producto_nuevo["cantidad"]
                else:
                    inventario.append(producto_nuevo)

            print("Inventario fusionado correctamente")

        else:
            print("Opción inválida, no se realizaron cambios")


    # Saliendo del bucle  
    
    elif seleccion == 9:
        print("Saliendo...\n")
        salir = True
    
    else:
        print("\nError, intenta de nuevo")






