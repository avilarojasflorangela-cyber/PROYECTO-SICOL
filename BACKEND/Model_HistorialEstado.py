from Conexionbasededatos import ConexionMysql
class Model_HistorialEstado:
    def __init__(self):
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion 
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos

    def obtener_historial_estado(self, id_pedido):
        self.cursor.execute("SELECT * FROM historial_estado WHERE id=%s", (id_pedido,))
        return self.cursor.fetchone()

    def obtener_historial_estados(self):
        self.cursor.execute("SELECT * FROM historial_estado")
        return self.cursor.fetchall()

    def insertar_historial_estado(self, estado, id_pedido):
        val = (estado,  id_pedido)
        sql = "INSERT INTO historial_estado (estado, id_pedido) VALUES (%s,%s)"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def cambiar_estado(self, id_pedido, estado):
        self.cursor.execute("UPDATE crear_pedido SET estado_pedido=%s WHERE id=%s", (estado, id_pedido))

        if self.cursor.rowcount == 0:
            return False

        self.cursor.execute("INSERT INTO historial_estado (id_pedido, estado) VALUES (%s,%s)", (id_pedido, estado))
        self.conexion.commit()
        return True

    
