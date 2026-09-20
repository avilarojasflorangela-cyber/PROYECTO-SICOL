from Conexionbasededatos import ConexionMysql
class Model_DocumentosProveedor:
    def __init__(self):
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos

    def obtener_documento_proveedor(self,id):
        self.cursor.execute("SELECT * FROM documentos_proveedor WHERE id=%s", (id,))
        return self.cursor.fetchone()

    def obtener_documentos_proveedor(self):
        self.cursor.execute("SELECT * FROM documentos_proveedor")
        return self.cursor.fetchall()

    def insertar_documento_proveedor(self, tipo_documento, nombre_archivo, ruta_archivo, fecha_subida, estado_validacion, id_proveedor):
        val = (tipo_documento, nombre_archivo, ruta_archivo, fecha_subida, estado_validacion, id_proveedor)
        sql = "INSERT INTO documentos_proveedor (tipo_documento, nombre_archivo, ruta_archivo, fecha_subida, estado_validacion, id_proveedor) VALUES (%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def actualizar_documento_proveedor(self, id, tipo_documento, nombre_archivo, ruta_archivo, fecha_subida, estado_validacion, id_proveedor):
        val = (tipo_documento, nombre_archivo, ruta_archivo, fecha_subida, estado_validacion, id_proveedor, id)
        sql = "UPDATE documentos_proveedor SET tipo_documento=%s, nombre_archivo=%s, ruta_archivo=%s, fecha_subida=%s, estado_validacion=%s, id_proveedor=%s WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def actualizar_estado_documento(self, id, estado_validacion):
        val = (estado_validacion, id)
        sql = "UPDATE documentos_proveedor SET estado_validacion=%s WHERE id=%s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def eliminar_documento_proveedor(self,id):
        val = (id,)
        sql = "DELETE FROM documentos_proveedor WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def documentos_proveedor(self):
        self.cursor.execute("""
        SELECT 
            proveedores.id AS id_proveedor,
            proveedores.razon_social AS razon_social,
            proveedores.ciudad AS ciudad,
            proveedores.forma_pago AS forma_pago
        FROM documentos_proveedor
        INNER JOIN proveedores 
            ON documentos_proveedor.id_proveedor = proveedores.id
        """)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
