from config import obtener_conexion

def Register (
        codigo,
        nombre,
        costo,
        precio_venta,
        stock,
        ubicacion,
        estado,
        imagenes,
        calificacion,
        cod_subcategoria):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO productos(CODIGO, NOMBRE, COSTO, PRECIO_VENTA, STOCK, UBICACION, ESTADO, IMAGENES, CALIFICACION, COD_SUBCATEGORIA) "
                        + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (codigo,nombre,costo,precio_venta,stock,ubicacion, estado,imagenes,calificacion,
                        cod_subcategoria))
    conexion.commit()
    conexion.close()