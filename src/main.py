from saludo.bienvenida import bienvenida_usuario
from detalle.datos_venta import precio_producto, cantidad_producto 
inventario = []
opcion = 1

bienvenida_usuario()

while opcion < 3:

    print("---------------------------  MENU  -------------------------")
    print("-"*60 )
    print("|          1.<---- Ingresar venta.                        |")
    print("|          2.<---- Visualizar ventas.                     |")
    print("|          3.<---- Salir.                                 |")
    print("-"*60)

    opcion = int(input("Ingrese la opcion que va a elegir \n"))

    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del producto \n  ")

            precio=precio_producto()

            cantidad=cantidad_producto()

            subtotal = precio * cantidad
            print("El resumen de su venta:")
            print(f"PRODUCTO: {nombre}")
            print(f"CANTIDAD: {cantidad} unidad(es)")
            print(f"PRECIO:   {precio} Pesos")
            print(" El subtotal es:", subtotal)

            # crear el diccionario producto_nuevo
            producto_nuevo = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad,
                "subtotal":subtotal
            }
            inventario.append(producto_nuevo)
        case 2:
            if len(inventario)==0:
                print("-"*60)
                print("\n No hay datos para mostrar. \n")
                print("-"*60)

            else:
                print("-"*60)

                print(f"\n {inventario}")
        case 3:
            print("Saliendo del sistema")