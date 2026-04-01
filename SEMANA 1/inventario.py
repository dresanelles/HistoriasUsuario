#Sistema de inventario


# Solicitud de datos al usuario

nombre = input("Nombre del producto: ")


# Creación de bucles para evitar errores en la introducción de datos en precio y cantidad

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



#Calculo del costo total

costo_total = precio * cantidad


# Mostrar resultados en consola
print("\n------ INVENTARIO -----\n")
print(f'Nombre del producto: {nombre}\nPrecio unitario: {precio}\nCantidad: {cantidad}\nCosto total calculado: {costo_total}\n')


## Este programa simula la gestión de inventario de un producto, el cual es ejecutado siguiendo una secuencia de solicitud de datos de forma obligatoria como lo son: Nombre del producto, Precio y Cantidad. Se debe indicar si existe un error al momento de ingresar los valores en precio y cantidad y repetirlo hasta que el usuario ingrese los datos correctos a cada item. Además, se deberá hacer el calculo del costo total del inventario realizando la operación del precio ingresado multiplicado por la cantidad disponible. Finalmente, muestra de forma clara el inventario con sus items y valores respectivamente.