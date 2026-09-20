import mysql.connector
from mysql.connector import Error

class ConexionMysql:
    def __init__(self):
        try:
            self.mibasededatos = mysql.connector.connect(
                host="localhost",
                port= "3306",
                user="root",
                password= "Flor123*",
                database="sicol"
        )
            self.conexion = self.mibasededatos
            self.conexion.autocommit = True
            self.cursor = self.conexion.cursor(buffered=True)
            if self.mibasededatos.is_connected():
                db_Info = self.mibasededatos.get_server_info()
                print(f"Conectada con mi base de datos, version:, {db_Info}")
        except Error as e:
            print(f"Error al conectar Mysql: {e}")

    def cerrar_conexion(self):
        if hasattr(self, 'mibasededatos') and self.mibasededatos.is_connected():
            self.cursor.close()
            self.conexion.close()
            print("Conexión cerrada correctamente")

if __name__ == "__main__":
    conexion = ConexionMysql()
    conexion.cerrar_conexion()
