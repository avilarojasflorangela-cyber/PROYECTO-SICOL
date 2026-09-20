from Conexionbasededatos import ConexionMysql
class Model_DetalleProducto:
    def __init__(self):
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos

    def obtener_detalle_producto(self,cod_producto):
        self.cursor.execute("SELECT * FROM detalle_producto WHERE cod_producto=%s", (cod_producto,))
        return self.cursor.fetchone()

    def obtener_detalle_productos(self):
        self.cursor.execute("SELECT * FROM detalle_producto")
        return self.cursor.fetchall()

    def obtener_por_id(self, id):
        self.cursor.execute("SELECT * FROM detalle_producto WHERE id=%s", (id,))
        return self.cursor.fetchone()

    def obtener_por_codigo(self, cod_producto):
        self.cursor.execute("SELECT * FROM detalle_producto WHERE cod_producto=%s", (cod_producto,))
        return self.cursor.fetchone()

    def desactivar_detalle_producto(self, id):
        self.cursor.execute("UPDATE detalle_producto SET estado_producto = 'Desactivo' WHERE id=%s", (id,))
        self.conexion.commit()

    def insertar_detalle_producto(self, nombre_producto, descripcion, unidad_medida, precio_unitario, estado_producto, categoria, marca, cod_producto):
        val = (nombre_producto, descripcion, unidad_medida, precio_unitario, estado_producto, categoria, marca, cod_producto)
        sql = "INSERT INTO detalle_producto  (nombre_producto, descripcion, unidad_medida, precio_unitario, estado_producto, categoria, marca, cod_producto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def actualizar_detalle_producto(self, id, nombre_producto, descripcion, unidad_medida, precio_unitario, estado_producto, categoria, marca, cod_producto):
        val = (nombre_producto, descripcion, unidad_medida, precio_unitario, estado_producto, categoria, marca, cod_producto, id)
        sql = "UPDATE detalle_producto SET nombre_producto=%s, descripcion=%s, unidad_medida=%s, precio_unitario=%s, estado_producto=%s, categoria=%s, marca=%s, cod_producto=%s WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def eliminar_detalle_producto(self,id):
        val = (id,)
        sql = "DELETE FROM detalle_producto WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
