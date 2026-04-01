import json
import os

def guardarJson(inventario):

    if len(inventario) == 0:
        print("No hay datos para guardar")
        return
    
    try:
        with open("inventario.json", "w") as archivo:
            json.dump(inventario, archivo)
        
        print("Inventario guardado correctamente")
    except:
        print("Error al guardar el archivo")

def cargarJson():
    

    try:
        print("Ruta del archivo:", os.path.abspath("inventario.json"))
        with open("inventario.json", "r") as archivo:
            inventario = json.load(archivo)
        
        print("Inventario cargado correctamente")
        return inventario
    except Exception as e:
        print(f"Error al cargar: {e}")
        return[]
