from saludo.bienvenida import bienvenida_usuario, menu_inicio
from detalle.helpers import (
    insertar_producto,
    visualizar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas,
    guardar_csv,
    cargar_csv
)

inventario = []

opcion = 0

bienvenida_usuario()

while opcion != 9:
    menu_inicio()

    while True:
        try:
            opcion = int(input("Ingrese la opción que va a elegir: \n"))
            if opcion < 1 or opcion > 9:
                print("Ingrese una opción válida entre 1 y 9.")
            else:
                break
        except ValueError:
            print("Ingrese un número válido.")

    print("-" * 60)

    if opcion == 1:
        print("===================== AGREGAR PRODUCTO =====================")
        insertar_producto(inventario)

    elif opcion == 2:
        print("=================== MOSTRAR INVENTARIO =====================")
        visualizar_inventario(inventario)

    elif opcion == 3:
        print("==================== BUSCAR PRODUCTO =======================")
        nombre_producto = input("Ingrese el nombre del producto: \n").upper()
        resultado = buscar_producto(inventario, nombre_producto)

        if resultado:
            print(f"PRODUCTO: {resultado['nombre']}")
            print(f"PRECIO: {resultado['precio']}")
            print(f"CANTIDAD: {resultado['cantidad']}")
            print("-" * 60)

    elif opcion == 4:
        print("=================== ACTUALIZAR PRODUCTO ====================")
        nombre_producto = input("Ingrese el nombre del producto a actualizar: \n").upper()
        actualizar_producto(inventario, nombre_producto)

    elif opcion == 5:
        print("==================== ELIMINAR PRODUCTO =====================")
        nombre_producto = input("Ingrese el nombre del producto a eliminar: \n").upper()
        eliminar_producto(inventario, nombre_producto)

    elif opcion == 6:
        print("==================== ESTADÍSTICAS ==========================")
        estadisticas = calcular_estadisticas(inventario)

        if estadisticas:
            print(f"Unidades totales: {estadisticas['unidades_totales']}")
            print(f"Valor total inventario: ${estadisticas['valor_total']}")
            print(f"Producto más caro: {estadisticas['producto_mas_caro']['nombre']} - ${estadisticas['producto_mas_caro']['precio']}")
            print(f"Producto con mayor stock: {estadisticas['producto_mayor_stock']['nombre']} - {estadisticas['producto_mayor_stock']['cantidad']} unidades")
            print("-" * 60)

    elif opcion == 7:
        print("====================== GUARDAR CSV =========================")
        guardar_csv(inventario)

    elif opcion == 8:
        print("======================= CARGAR CSV =========================")
        inventario = cargar_csv(inventario)

    elif opcion == 9:
        print("Saliendo del sistema...")
        break