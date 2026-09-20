from Conexionbasededatos import ConexionMysql
class Model_EntradaMaterial:
    def __init__(self):
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos

    def obtener_entrada_material (self,id):
        self.cursor.execute("SELECT * FROM entrada_material WHERE id=%s", (id,))
        return self.cursor.fetchone()

    def obtener_entrada_materiales(self):
        self.cursor.execute("SELECT * FROM entrada_material")
        return self.cursor.fetchall()

    def obtener_entradas_por_orden(self, id_orden):
        self.cursor.execute("SELECT * FROM entrada_material WHERE id_orden=%s", (id_orden,))
        return self.cursor.fetchall()

    def insertar_entrada_material(self, fecha_entrada, cantidad_recibida, recibido_por, cumplimiento_orden_compra, observaciones, id_orden, cod_producto):
        val = (fecha_entrada, cantidad_recibida, recibido_por, cumplimiento_orden_compra, observaciones, id_orden, cod_producto)
        sql = "INSERT INTO entrada_material (fecha_entrada, cantidad_recibida, recibido_por, cumplimiento_orden_compra, observaciones, id_orden, cod_producto) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def actualizar_entrada_material(self, id, fecha_entrada, cantidad_recibida, recibido_por, cumplimiento_orden_compra, observaciones, id_orden, cod_producto):
        val = (fecha_entrada, cantidad_recibida, recibido_por, cumplimiento_orden_compra, observaciones, id_orden, cod_producto, id)
        sql = "UPDATE entrada_material SET fecha_entrada=%s, cantidad_recibida=%s, recibido_por=%s, cumplimiento_orden_compra=%s, observaciones=%s, id_orden=%s, cod_producto=%s WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def eliminar_entrada_material(self,id):
        val = (id,)
        sql = "DELETE FROM entrada_material WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def entrada_material(self):
        self.cursor.execute("""
        SELECT 
            orden_compra.id AS id_orden_compra,
            orden_compra.cantidad AS cantidad,
            proveedores.razon_social AS razon_social,
            orden_compra.id_pedido AS id_pedido,
            detalle_producto.cod_producto AS cod_producto,
            detalle_producto.nombre_producto AS nombre_producto,
            COALESCE(SUM(entrada_material.cantidad_recibida), 0) AS cantidad_recibida
        FROM orden_compra
        INNER JOIN proveedores
            ON orden_compra.id_proveedor = proveedores.id
        INNER JOIN detalle_producto
            ON orden_compra.cod_producto = detalle_producto.cod_producto
        LEFT JOIN entrada_material
        ON orden_compra.id = entrada_material.id_orden
        GROUP BY 
            orden_compra.id,
            orden_compra.cantidad, 
            proveedores.razon_social,
            orden_compra.id_pedido,
            detalle_producto.cod_producto, 
            detalle_producto.nombre_producto
        """)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()