from Conexionbasededatos import ConexionMysql
class Model_CrearPedido:
    def __init__(self):
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos

    def obtener_crear_pedido (self,id):
        self.cursor.execute("SELECT * FROM crear_pedido WHERE id=%s", (id,))
        return self.cursor.fetchone()

    def obtener_crear_pedidos(self):
        self.cursor.execute("SELECT * FROM crear_pedido")
        return self.cursor.fetchall()

    def insertar_crear_pedido(self, fecha_creacion, nombre_producto, cantidad, destino, fecha_requerida, estado_pedido, id_usuario, cod_producto):
        val = (fecha_creacion, nombre_producto, cantidad, destino, fecha_requerida, estado_pedido, id_usuario, cod_producto)
        sql = "INSERT INTO crear_pedido (fecha_creacion, nombre_producto, cantidad, destino, fecha_requerida, estado_pedido, id_usuario, cod_producto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql, val)
        self.conexion.commit()
        return self.cursor.lastrowid

    def actualizar_crear_pedido(self, id, fecha_creacion, nombre_producto, cantidad, destino, fecha_requerida, estado_pedido, id_usuario, cod_producto):
        val = (fecha_creacion, nombre_producto, cantidad, destino, fecha_requerida, estado_pedido, id_usuario, cod_producto, id )
        sql = "UPDATE crear_pedido SET fecha_creacion=%s, nombre_producto=%s, cantidad=%s, destino=%s, fecha_requerida=%s, estado_pedido=%s, id_usuario=%s, cod_producto=%s WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def eliminar_crear_pedido(self,id):
        val = (id,)
        sql = "DELETE FROM crear_pedido WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def crear_pedido(self):
        self.cursor.execute("""
        SELECT
            usuarios.Usua_Nombre AS Usua_Nombre,
            usuarios.Usua_Apellido AS Usua_Apellido,
            usuarios.Usua_Correo AS Usua_Correo,
            usuarios.Usua_Area AS Usua_Area,
            detalle_producto.cod_producto AS cod_producto,
            detalle_producto.categoria AS categoria
        FROM crear_pedido
        INNER JOIN usuarios
            ON crear_pedido.id_usuario = usuarios.id
        INNER JOIN detalle_producto
            ON crear_pedido.cod_producto = detalle_producto.cod_producto
        """)
        return self.cursor.fetchall()

    def obtener_pedidos_logistica(self):
        self.cursor.execute("""
        SELECT  
            crear_pedido.id AS id_pedido,
            usuarios.Usua_Nombre AS Usua_Nombre,
            usuarios.Usua_Apellido AS Usua_Apellido,
            crear_pedido.fecha_creacion AS fecha_creacion,
            crear_pedido.nombre_producto AS nombre_producto,
            crear_pedido.cantidad AS cantidad,
            crear_pedido.destino AS destino,
            crear_pedido.fecha_requerida AS fecha_requerida,
            crear_pedido.estado_pedido AS estado_pedido
        FROM crear_pedido
        INNER JOIN usuarios
            ON crear_pedido.id_usuario = usuarios.id
        """)
        return self.cursor.fetchall()

    def reporte_pedidos(self):
        self.cursor.execute("""
        SELECT
            crear_pedido.id AS id_pedido,
            usuarios.Usua_Nombre AS usuario,
            crear_pedido.fecha_creacion AS fecha_creacion,
            crear_pedido.nombre_producto AS nombre_pedido,
            crear_pedido.cantidad AS cantidad,
            crear_pedido.destino AS destino,
            crear_pedido.fecha_requerida AS fecha_requerida,
            crear_pedido.estado_pedido AS estado_pedido,
            detalle_producto.cod_producto AS cod_producto,
            detalle_producto.descripcion AS descripcion,
            detalle_producto.marca AS marca
        FROM crear_pedido
        INNER JOIN usuarios
            ON crear_pedido.id_usuario = usuarios.id
        INNER JOIN detalle_producto
            ON crear_pedido.cod_producto = detalle_producto.cod_producto
        """)
        return self.cursor.fetchall()

    def cerrar_conexion (self): 
        self.cursor.close()
        self.conexion.close()