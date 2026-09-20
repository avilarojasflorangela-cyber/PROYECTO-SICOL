from Conexionbasededatos import ConexionMysql
class Model_Empleados:
    def __init__(self):
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion 
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos

    def obtener_empleado (self,id):
        self.cursor.execute("SELECT * FROM empleados WHERE id=%s", (id,))
        return self.cursor.fetchone()

    def obtener_empleados (self):
        self.cursor.execute("SELECT * FROM empleados")
        return self.cursor.fetchall()

    def insertar_empleado(self, ID_CC , Cargo_usuario, Estado_usuario, Fecha_ingreso, area_asignada, id_usuario):
        val = (ID_CC, Cargo_usuario, Estado_usuario, Fecha_ingreso, area_asignada, id_usuario)
        sql = "INSERT INTO empleados (ID_CC, Cargo_usuario, Estado_usuario, Fecha_ingreso, area_asignada, id_usuario) VALUES (%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def actualizar_empleado(self, id, ID_CC, Cargo_usuario, Estado_usuario, Fecha_ingreso, area_asignada, id_usuario):
        val = (ID_CC, Cargo_usuario, Estado_usuario, Fecha_ingreso, area_asignada, id_usuario, id)
        sql = "UPDATE empleados SET ID_CC=%s, Cargo_usuario=%s, Estado_usuario=%s, Fecha_ingreso=%s, area_asignada=%s, id_usuario=%s WHERE id=%s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def eliminar_empleado(self,id):
        val = (id,)
        sql = "DELETE FROM empleados WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def empleados(self):
        self.cursor.execute("""
        SELECT
            usuarios.Usua_Nombre AS Usua_Nombre,
            usuarios.Usua_Apellido AS Usua_Apellido,
            usuarios.Uus_Correo AS Usua_Correo
        FROM empleados
        INNER JOIN usuarios
            ON empleados.id_usuario = usuarios.id
        """)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()