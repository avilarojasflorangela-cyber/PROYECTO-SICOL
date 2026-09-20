from Conexionbasededatos import ConexionMysql
class Model_Facturas:
    def __init__(self):
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos

    def obtener_factura(self,id):
        self.cursor.execute("SELECT * FROM facturas WHERE id=%s", (id,))
        return self.cursor.fetchone()

    def obtener_facturas(self):
        self.cursor.execute("SELECT * FROM facturas")
        return self.cursor.fetchall()

    def insertar_factura(self, fecha_radicacion, fecha_vencimiento, forma_pago, total_factura, estado_factura, observaciones, id_proveedor, id_orden):
        val = (fecha_radicacion, fecha_vencimiento, forma_pago, total_factura, estado_factura, observaciones, id_proveedor, id_orden)
        sql = "INSERT INTO facturas (fecha_radicacion, fecha_vencimiento, forma_pago, total_factura, estado_factura, observaciones, id_proveedor, id_orden) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def actualizar_factura(self, id, fecha_radicacion, fecha_vencimiento, forma_pago, total_factura, estado_factura, observaciones, id_proveedor, id_orden):
        val = (fecha_radicacion, fecha_vencimiento, forma_pago, total_factura, estado_factura, observaciones, id_proveedor, id_orden, id)
        sql = "UPDATE facturas SET fecha_radicacion=%s, fecha_vencimiento=%s, forma_pago=%s, total_factura=%s, estado_factura=%s, observaciones=%s, id_proveedor=%s, id_orden=%s WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def actualizar_estado_factura(self, id, estado_factura):
        val = (estado_factura, id)
        sql = "UPDATE facturas SET estado_factura=%s WHERE id=%s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def actualizar_observacion_factura(self, id, observaciones):
        val = (observaciones, id)
        sql = "UPDATE facturas SET observaciones=%s WHERE id=%s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def eliminar_factura(self, id):
        val = (id,)
        sql = "DELETE FROM facturas WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def facturas(self):
        self.cursor.execute("""
        SELECT 
            facturas.id AS id_factura,
            proveedores.ID_CC_NIT AS ID_CC_NIT,
            proveedores.razon_social AS razon_social,
            proveedores.nombre_asesor AS nombre_asesor,
            proveedores.correo_electronico AS correo_electronico,
            facturas.fecha_radicacion AS fecha_radicacion,
            facturas.fecha_vencimiento AS fecha_vencimiento,
            facturas.forma_pago AS forma_pago,
            facturas.estado_factura AS estado_factura,
            facturas.total_factura AS total_factura,
            facturas.observaciones AS observaciones,
            orden_compra.id AS id_orden,
            orden_compra.precio_unitario AS precio_unitario,
            orden_compra.cantidad AS cantidad
        FROM facturas
        INNER JOIN proveedores
            ON facturas.id_proveedor = proveedores.id
        INNER JOIN orden_compra
            ON facturas.id_orden = orden_compra.id
        """)
        return self.cursor.fetchall()

    def reporte_facturas(self):
        self.cursor.execute("""
        SELECT 
            facturas.id AS id_factura,
            facturas.fecha_radicacion AS fecha_radicacion,
            facturas.fecha_vencimiento AS fecha_vencimiento,
            facturas.forma_pago AS forma_pago,
            facturas.total_factura AS total_factura,
            facturas.estado_factura AS estado_factura,
            facturas.observaciones AS observaciones,
            proveedores.ID_CC_NIT AS ID_CC_NIT,
            proveedores.razon_social AS razon_social,
            proveedores.nombre_asesor AS nombre_asesor,
            proveedores.correo_electronico AS correo_electronico,
            proveedores.numero_telefono AS numero_telefono,
            proveedores.ciudad AS ciudad,
            orden_compra.id AS id_orden
        FROM facturas
        INNER JOIN proveedores 
            ON facturas.id_proveedor = proveedores.id
        INNER JOIN orden_compra
            ON facturas.id_orden = orden_compra.id
        """)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()