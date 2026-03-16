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

def detalle_venta():
    print("--- DETALLE DEL INVENTARIO ---")
    print(f"Producto: {producto['nombre']}")
    print(f"Precio:   {producto['precio']}")
    print(f"Cantidad: {producto['cantidad']}")
    print(f"Subtotal: {producto['subtotal']}")
    
    print("-" * 30)


