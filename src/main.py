from saludo.bienvenida import bienvenida_usuario
from detalle.datos_venta import precio_producto, cantidad_producto, detalle_venta
inventario = []
opcion = 1

bienvenida_usuario()

while opcion < 4:

    print("---------------------------  MENU  -------------------------")
    print("-"*60 )
    print("|          1.<---- Ingresar venta.                        |")
    print("|          2.<---- Visualizar ventas.                     |")
    print("|          3.<---- Calcular.                              |")
    print("|          4.<---- Salir.                                 |")

    
    print("-"*60)

    opcion = int(input("Ingrese la opcion que va a elegir \n"))

    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del producto \n").upper()

            precio = precio_producto()

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
            if len(inventario) == 0:
                print("-"*60)
                print("\n No hay datos para mostrar. \n")
                print("-"*60)

            else:
                print("-"*60)

                for i in inventario:
                    print(f"PRODUCTO: {i["nombre"]}")
                    print(f"PRECIO: {i["precio"]}")
                    print(f"CANTIDAD: {i["cantidad"]}")
                    print(f"SUBTOTAL: {i["subtotal"]}")
        case 3:
            #calcular
            print("calculo")
        case 4:
            print("Saliendo del sistema...")
