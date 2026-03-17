from saludo.bienvenida import bienvenida_usuario, menu_inicio
from detalle.helpers import calcular_estadistica, insertar_producto, visualizar_ventas

inventario = []
opcion = 1

def buscar_producto(inventario, producto_buscado):
    for producto in inventario:
        if producto["nombre"] == producto_buscado:
         return producto
    return None 

bienvenida_usuario()
# Empieza el bucle que hace que el menú funcione
while opcion != 0:
    menu_inicio()
    while True:
        try:
            opcion = int(input("Ingrese la opcion que va a elegir,\n"))
            break
        except ValueError:
            print("Ingrese un número valido.")

    print("-" * 60)

    if opcion == 1:
        print("===================== Agregar producto =====================")
        insertar_producto(inventario)

    elif opcion == 2:
        print("================= Visualizador de ventas ===================")
        if len(inventario) == 0:
            print("-" * 60)
            print("\n No hay datos para mostrar. \n")
            print("-" * 60)

        else:
            print("-" * 60)
            visualizar_ventas(inventario) 
    elif opcion == 3:
        total_dinero, total_unidades = calcular_estadistica(inventario)
        # Se desemapaqueto calcular_estadisticas
        print("================== CALCULO DE ESTADISTICA ==================")
        print(f"${total_dinero}, {total_unidades} Unidad(es)")
        print()

    elif opcion == 4:
       print("==================== BUSQUEDA PRODUCTOS =====================")
       nombre = input("Ingrese por favor el nombre del producto.\n")
       resultado = buscar_producto(inventario, nombre)
       print()

    elif opcion == 5:
        print("Saliendo del sistema...")
        break
