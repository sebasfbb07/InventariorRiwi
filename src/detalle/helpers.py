

def precio_producto():
    while True:
                try:
                    precio = float(input("Ingrese el precio del producto: \n"))
                    break
                except ValueError:
                    print(
                        "Error: Por favor, ingrese un valor numérico válido para precio.")
    return precio

def cantidad_producto():
    while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del producto: \n"))
                    break
                except ValueError:
                    print(
                        "Error: Por favor, ingrese un valor numérico válido para cantidad."
                    )
    return cantidad 

def insertar_producto(inventario):
        
    nombre = input("Ingrese el nombre del producto \n").upper()
    print()

    precio = precio_producto()
    print()

    cantidad = cantidad_producto()
    print()
    
    subtotal = precio * cantidad

    producto_nuevo = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "subtotal": subtotal,
    }
    inventario.append(producto_nuevo)
    print(f"✅ {nombre} agregado con éxito.")
    print()

def visualizar_ventas(inventario):
    for i in inventario:
        print(f"PRODUCTO: {i["nombre"]}")
        print(f"PRECIO: {i["precio"]}")
        print(f"CANTIDAD: {i["cantidad"]}")
        print(f"SUBTOTAL: {i["subtotal"]}")
        print()

# Funcion para calcular la estadistica 
def calcular_estadistica(inventario):
   if len(inventario) == 0:
        print("No hay productos en el inventario.")
        valor_total_sumado = 0
        cantidad_total_items = 0
        return valor_total_sumado, cantidad_total_items
   else:
        print("No hay productos en el inventario.")
        valor_total_sumado = 0
        cantidad_total_items = 0
        for producto_nuevo in inventario:
            valor_total_sumado += producto_nuevo["subtotal"]
            cantidad_total_items += producto_nuevo["cantidad"]
        return valor_total_sumado, cantidad_total_items


def buscar_producto(inventario, Nombre_buscado):
    for producto_nuevo in inventario:
        if producto_nuevo["nombre"] == Nombre_buscado:
            return producto_nuevo
    print()
    print(f"El producto {Nombre_buscado} no esta en la lista.")
    print() 
    return None
   

      


