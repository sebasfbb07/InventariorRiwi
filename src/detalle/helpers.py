import csv


def precio_producto():
    """
    Solicita y valida el precio del producto.
    Retorna un float no negativo.
    """
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: \n"))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                return precio
        except ValueError:
            print("Error: ingrese un valor numérico válido para el precio.")


def cantidad_producto():
    """
    Solicita y valida la cantidad del producto.
    Retorna un int no negativo.
    """
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: \n"))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                return cantidad
        except ValueError:
            print("Error: ingrese un valor numérico válido para la cantidad.")


def insertar_producto(inventario):
    """
    Agrega un producto al inventario.
    Si ya existe, no lo agrega repetido.
    """
    nombre = input("Ingrese el nombre del producto: \n").upper()

    producto_existente = buscar_producto(inventario, nombre)
    if producto_existente:
        print("Ese producto ya existe en el inventario.")
        return

    precio = precio_producto()
    cantidad = cantidad_producto()

    producto_nuevo = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto_nuevo)
    print(f"✅ {nombre} agregado con éxito.")
    print()


def visualizar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    """
    if len(inventario) == 0:
        print("No hay productos en el inventario.")
        print("-" * 60)
        return

    for producto in inventario:
        print(f"PRODUCTO: {producto['nombre']}")
        print(f"PRECIO: {producto['precio']}")
        print(f"CANTIDAD: {producto['cantidad']}")
        print(f"SUBTOTAL: {producto['precio'] * producto['cantidad']}")
        print("-" * 60)


def buscar_producto(inventario, nombre_buscado):
    """
    Busca un producto por nombre.
    Retorna el diccionario del producto o None si no existe.
    """
    for producto in inventario:
        if producto["nombre"] == nombre_buscado:
            return producto

    print(f"El producto {nombre_buscado} no está en el inventario.")
    print("-" * 60)
    return None


def actualizar_producto(inventario, nombre_buscado):
    """
    Actualiza el precio y/o cantidad de un producto.
    """
    producto = buscar_producto(inventario, nombre_buscado)

    if producto:
        print("Deje vacío si no desea cambiar ese valor.")

        nuevo_precio = input("Ingrese el nuevo precio: \n")
        nueva_cantidad = input("Ingrese la nueva cantidad: \n")

        if nuevo_precio != "":
            try:
                nuevo_precio = float(nuevo_precio)
                if nuevo_precio >= 0:
                    producto["precio"] = nuevo_precio
                else:
                    print("El precio no puede ser negativo.")
            except ValueError:
                print("Precio inválido. No se actualizó.")

        if nueva_cantidad != "":
            try:
                nueva_cantidad = int(nueva_cantidad)
                if nueva_cantidad >= 0:
                    producto["cantidad"] = nueva_cantidad
                else:
                    print("La cantidad no puede ser negativa.")
            except ValueError:
                print("Cantidad inválida. No se actualizó.")

        print("✅ Producto actualizado correctamente.")
        print("-" * 60)


def eliminar_producto(inventario, nombre_buscado):
    """
    Elimina un producto del inventario por nombre.
    """
    producto = buscar_producto(inventario, nombre_buscado)

    if producto:
        inventario.remove(producto)
        print(f"🗑️ Producto {nombre_buscado} eliminado correctamente.")
        print("-" * 60)


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario:
    - unidades totales
    - valor total
    - producto más caro
    - producto con mayor stock
    Retorna un diccionario con los resultados.
    """
    if len(inventario) == 0:
        print("No hay productos en el inventario.")
        print("-" * 60)
        return None

    unidades_totales = 0
    valor_total = 0

    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]

    for producto in inventario:
        unidades_totales += producto["cantidad"]
        valor_total += producto["precio"] * producto["cantidad"]

        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    estadisticas = {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }

    return estadisticas


def guardar_csv(inventario):
    """
    Guarda el inventario en un archivo CSV.
    """
    if len(inventario) == 0:
        print("No hay productos para guardar.")
        print("-" * 60)
        return

    nombre_archivo = "data/inventario.csv"
    campos = ["nombre", "precio", "cantidad"]

    try:
        with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(inventario)

        print(f"Inventario guardado en: {nombre_archivo}")
        print("-" * 60)

    except PermissionError:
        print("Error: no tienes permisos para escribir el archivo.")
    except Exception as e:
        print(f"Ocurrió un error al guardar: {e}")


def cargar_csv(inventario_actual):
    """
    Carga productos desde un archivo CSV.
    Permite sobrescribir o fusionar con el inventario actual.
    """
    nombre_archivo = "data/inventario.csv"
    inventario_cargado = []
    filas_invalidas = 0

    try:
        with open(nombre_archivo, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            if lector.fieldnames != ["nombre", "precio", "cantidad"]:
                print("Error: el archivo no tiene el encabezado correcto.")
                return inventario_actual

            for fila in lector:
                try:
                    nombre = fila["nombre"].upper()
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])

                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    producto = {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    }

                    inventario_cargado.append(producto)

                except ValueError:
                    filas_invalidas += 1

    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV.")
        return inventario_actual
    except UnicodeDecodeError:
        print("Error: el archivo tiene problemas de codificación.")
        return inventario_actual
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo: {e}")
        return inventario_actual

    if len(inventario_cargado) == 0:
        print("No se cargaron productos válidos.")
        return inventario_actual

    decision = input("¿Sobrescribir inventario actual? (S/N): \n").upper()

    if decision == "S":
        inventario_actual = inventario_cargado
        print("Inventario reemplazado correctamente.")
        accion = "Reemplazo"

    elif decision == "N":
        for producto_cargado in inventario_cargado:
            producto_existente = buscar_producto(inventario_actual, producto_cargado["nombre"])

            if producto_existente:
                producto_existente["cantidad"] += producto_cargado["cantidad"]
                producto_existente["precio"] = producto_cargado["precio"]
            else:
                inventario_actual.append(producto_cargado)

        print("Inventario fusionado correctamente.")
        accion = "Fusión"

    else:
        print("Opción inválida. No se realizaron cambios.")
        return inventario_actual

    print("-" * 60)
    print(f"Productos cargados: {len(inventario_cargado)}")
    print(f"Filas inválidas omitidas: {filas_invalidas}")
    print(f"Acción realizada: {accion}")
    print("-" * 60)

    return inventario_actual