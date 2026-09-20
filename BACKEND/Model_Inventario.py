from Conexionbasededatos import ConexionMysql
class Model_Inventario:
    def __init__(self):
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos

    def obtener_inventario(self,id):
        self.cursor.execute ("SELECT * FROM inventario WHERE id=%s", (id,))
        return self.cursor.fetchone()

    def obtener_inventarios(self):
        self.cursor.execute ("SELECT * FROM inventario")
        return self.cursor.fetchall()

    def obtener_por_producto(self, cod_producto):
        self.cursor.execute("SELECT * FROM inventario WHERE cod_producto=%s", (cod_producto,))
        return self.cursor.fetchone()

    def insertar_inventario (self, nombre_producto, cantidad, fecha_ingreso_material, tipo_movimiento, stock_minimo, id_orden, cod_producto):
        val = (nombre_producto, cantidad, fecha_ingreso_material, tipo_movimiento, stock_minimo, id_orden, cod_producto)
        sql = "INSERT INTO inventario (nombre_producto, cantidad, fecha_ingreso_material, tipo_movimiento, stock_minimo, id_orden, cod_producto) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def actualizar_inventario (self, id, nombre_producto, cantidad, fecha_ingreso_material, tipo_movimiento, stock_minimo, id_orden, cod_producto):
        val = (nombre_producto, cantidad, fecha_ingreso_material, tipo_movimiento, stock_minimo, id_orden, cod_producto, id)
        sql = "UPDATE inventario SET nombre_producto=%s, cantidad=%s, fecha_ingreso_material=%s, tipo_movimiento=%s, stock_minimo=%s, id_orden=%s, cod_producto=%s WHERE id=%s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def actualizar_cantidad(self, cod_porducto, cantidad):
        val = (cantidad, cod_porducto)
        sql = "UPDATE inventario SET cantidad=%s WHERE cod_producto=%s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def eliminar_inventario(self,id):
        val = (id,)
        sql = "DELETE FROM inventario WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def inventario(self):
        self.cursor.execute("""
        SELECT
            inventario.id AS id_inventario,
            orden_compra.id AS id_orden,
            proveedores.razon_social AS razon_social,
            detalle_producto.cod_producto AS cod_producto,
            detalle_producto.nombre_producto AS nombre_producto,
            inventario.cantidad AS cantidad,
            inventario.fecha_ingreso_material AS fecha_ingreso_material,
            inventario.tipo_movimiento AS tipo_movimiento,
            inventario.stock_minimo AS stock_minimo,
            detalle_producto.precio_unitario AS precio_unitario,
            detalle_producto.categoria AS categoria,
            detalle_producto.marca AS marca
        FROM inventario
        INNER JOIN orden_compra
            ON inventario.id_orden = orden_compra.id
        INNER JOIN proveedores
            ON orden_compra.id_proveedor = proveedores.id
        INNER JOIN detalle_producto
            ON inventario.cod_producto = detalle_producto.cod_producto
        """) 
        return self.cursor.fetchall()

    def reporte_invetario(self):
        self.cursor.execute("""
        SELECT 
            inventario.id AS id_inventario,
            inventario.nombre_producto AS nombre_producto,
            inventario.cantidad AS cantidad,
            inventario.fecha_ingreso_material AS fecha_ingreso_material,
            inventario.tipo_movimiento AS tipo_movimiento,
            inventario.stock_minimo AS stock_minimo,
            orden_compra.id AS id_orden,
            proveedores.razon_social AS razon_social,
            detalle_producto.cod_producto AS cod_producto,
            detalle_producto.precio_unitario AS precio_unitario,
            detalle_producto.categoria AS categoria,
            detalle_producto.marca AS marca
        FROM inventario
        INNER JOIN orden_compra
            ON inventario.id_orden = orden_compra.id
        INNER JOIN proveedores
            ON orden_compra.id_proveedor = proveedores.id
        INNER JOIN detalle_producto
            ON inventario.cod_producto = detalle_producto.cod_producto
        """)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()