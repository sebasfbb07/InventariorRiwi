from saludo.bienvenida import bienvenida_usuario, menu_inicio
from detalle.helpers import calcular_estadistica, insertar_producto, visualizar_ventas, buscar_producto, guardar_csv

inventario = []

opcion = 1

bienvenida_usuario()    

# Empieza el bucle que hace que el menú funcione
while opcion != 0:
    menu_inicio()
    while True:
        try:
            opcion = int(input("Ingrese la opcion que va a elegir: \n"))
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
        valor_total_sumado, cantidad_total_items = calcular_estadistica(inventario)
        # Se desemapaqueto calcular_estadisticas
        print("================== CALCULO DE ESTADISTICA ==================")           
        print(f"Valor total del inventario: ${valor_total_sumado}\n {cantidad_total_items} Unidad(es)")
        print()

    elif opcion == 4:
       print("==================== BUSQUEDA PRODUCTOS =====================")
       Nombre_producto = input("Ingrese el nombre del producto: \n").upper()
       resultado = buscar_producto(inventario, Nombre_producto)
       if resultado:
           print(f"Producto encontrado: {resultado["nombre"]}")
           print(f"PRECIO: {resultado["precio"]}")
           print(f"CANTIDAD: {resultado["cantidad"]}")
           print()
    elif opcion == 5:
        guardar_csv(inventario)

    elif opcion == 6:
        print("Saliendo del sistema...")
        break
