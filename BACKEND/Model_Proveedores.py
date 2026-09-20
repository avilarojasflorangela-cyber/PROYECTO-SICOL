from Conexionbasededatos import ConexionMysql
class Model_Proveedores:
    def __init__(self):
        self.mibasededatos = ConexionMysql()    
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos

    def obtener_proveedor (self,id):
        self.cursor.execute ("SELECT * FROM proveedores WHERE id=%s", (id,))
        return self.cursor.fetchone()

    def obtener_proveedores(self):
        self.cursor.execute("SELECT * FROM proveedores")
        return self.cursor.fetchall()


    def insertar_proveedor(self, ID_CC_NIT, razon_social, nombre_asesor, correo_electronico, numero_telefono, ciudad, pais, forma_pago, estado, id_usuario):
        val = (ID_CC_NIT, razon_social, nombre_asesor, correo_electronico, numero_telefono, ciudad, pais, forma_pago, estado, id_usuario)
        sql = "INSERT INTO proveedores (ID_CC_NIT, razon_social, nombre_asesor, correo_electronico, numero_telefono, ciudad, pais, forma_pago, estado, id_usuario) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def actualizar_proveedor(self, id, ID_CC_NIT, razon_social, nombre_asesor, correo_electronico, numero_telefono, ciudad, pais, forma_pago, estado, id_usuario):
        val = (ID_CC_NIT, razon_social, nombre_asesor, correo_electronico, numero_telefono, ciudad, pais, forma_pago, estado, id_usuario, id)
        sql = "UPDATE proveedores SET ID_CC_NIT=%s, razon_social=%s, nombre_asesor=%s, correo_electronico=%s, numero_telefono=%s, ciudad=%s, pais=%s, forma_pago=%s, estado=%s, id_usuario=%s WHERE id=%s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def actualizar_estado_proveedor(self, id, estado):
        val = (estado, id)
        sql = "UPDATE proveedores SET estado=%s WHERE id=%s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def eliminar_proveedor(self,id):
        val = (id,)
        sql = "DELETE FROM proveedores WHERE id=%s"
        self.cursor.execute(sql, val)
        self.conexion.commit()


    def reporte_proveedores(self):
        self.cursor.execute("""
        SELECT 
            id,
            ID_CC_NIT,
            razon_social,
            nombre_asesor,
            correo_electronico,
            numero_telefono,
            ciudad,
            pais,
            forma_pago,
            estado,
            id_usuario
        FROM proveedores 
        """)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()