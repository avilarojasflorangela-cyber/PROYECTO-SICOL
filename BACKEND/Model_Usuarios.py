from Conexionbasededatos import ConexionMysql
from werkzeug.security import generate_password_hash
class Model_Usuarios:
    def __init__(self):
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos

    def obtener_usuario(self,id):
        self.cursor.execute ("SELECT * FROM usuarios WHERE id=%s", (id,))
        return self.cursor.fetchone()

    def obtener_usuarios(self):
        self.cursor.execute ("SELECT * FROM usuarios")
        return self.cursor.fetchall()

    def insertar_usuario(self, ID_CC, Usua_Nombre, Usua_Apellido, Usua_Ciudad, Usua_Telefono, Usua_Correo, Usua_Estado, Usua_Area, contrasena):
        contrasena_hash = generate_password_hash(contrasena)
        val = (ID_CC, Usua_Nombre, Usua_Apellido, Usua_Ciudad, Usua_Telefono, Usua_Correo, Usua_Estado, Usua_Area, contrasena_hash)
        sql = "INSERT INTO usuarios (ID_CC, Usua_Nombre, Usua_Apellido, Usua_Ciudad, Usua_Telefono, Usua_Correo, Usua_Estado, Usua_Area, contrasena) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def actualizar_usuario(self, id, ID_CC, Usua_Nombre, Usua_Apellido, Usua_Ciudad, Usua_Telefono, Usua_Correo, Usua_Estado, Usua_Area, contrasena):
        if contrasena == "":
            self.cursor.execute(
                "SELECT contrasena FROM usuarios WHERE id=%s", (id,)
            )
            contrasena = self.cursor.fetchone()[0]
        else:
            contrasena = generate_password_hash(contrasena)
        val = (ID_CC, Usua_Nombre, Usua_Apellido, Usua_Ciudad, Usua_Telefono, Usua_Correo, Usua_Estado, Usua_Area, contrasena, id)
        sql = "UPDATE usuarios SET ID_CC=%s, Usua_Nombre=%s, Usua_Apellido=%s, Usua_Ciudad=%s, Usua_Telefono=%s, Usua_Correo=%s, Usua_Estado=%s, Usua_Area=%s, contrasena=%s WHERE id=%s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def eliminar_usuario(self,id):
        val = (id,)
        sql = "DELETE FROM usuarios WHERE id=%s"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def verificarUsuario(self, ID_CC):
        val = (ID_CC,)
        sql ="SELECT id, ID_CC, Usua_Nombre, Usua_Apellido, Usua_Correo, Usua_Area, contrasena FROM usuarios WHERE ID_CC=%s"
        self.cursor.execute(sql, val)
        return self.cursor.fetchone()
