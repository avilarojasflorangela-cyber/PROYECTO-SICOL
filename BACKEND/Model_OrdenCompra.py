from Conexionbasededatos import ConexionMysql
class  Model_OrdenCompra:
    def __init__(self):
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos

    def obtener_orden_compra(self,id):
        self.cursor.execute("SELECT * FROM orden_compra WHERE id=%s", (id,))
        return self.cursor.fetchone()

    def obtener_orden_compras(self):
        self.cursor.execute("SELECT * FROM orden_compra")
        return self.cursor.fetchall()
    
    def insertar_orden_compra(self, precio_unitario, cantidad, fecha_orden, fecha_entrega,  estado_orden, observaciones, id_proveedor, cod_producto, id_pedido):
        val = (precio_unitario, cantidad, fecha_orden, fecha_entrega, estado_orden, observaciones, id_proveedor, cod_producto, id_pedido)
        sql = "INSERT INTO orden_compra (precio_unitario, cantidad, fecha_orden, fecha_entrega,  estado_orden, observaciones, id_proveedor, cod_producto, id_pedido) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,val)
        id_orden = self.cursor.lastrowid
        self.conexion.commit()
        return id_orden

    def actualizar_orden_compra(self, id, precio_unitario, cantidad, fecha_orden, fecha_entrega, estado_orden, observaciones, id_proveedor, cod_producto, id_pedido ):
        val = (precio_unitario, cantidad, fecha_orden, fecha_entrega,  estado_orden, observaciones, id_proveedor, cod_producto, id_pedido, id)
        sql = "UPDATE orden_compra SET precio_unitario=%s, cantidad=%s, fecha_orden=%s, fecha_entrega=%s, estado_orden=%s, observaciones=%s, id_proveedor=%s, cod_producto=%s, id_pedido=%s WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def eliminar_orden_compra(self,id):
        val = (id,)
        sql = "DELETE FROM orden_compra WHERE id=%s"
        self.cursor.execute(sql,val)
        self.conexion.commit()

    def obtener_orden_compras(self):
        self.cursor.execute("""
        SELECT 
            orden_compra.id AS id_orden,
            crear_pedido.id AS id_pedido,
            proveedores.razon_social AS razon_social,
            detalle_producto.nombre_producto AS nombre_producto,
            orden_compra.cantidad AS cantidad,
            orden_compra.precio_unitario AS precio_unitario,
            orden_compra.fecha_orden AS fecha_orden,
            orden_compra.fecha_entrega AS fecha_entrega,
            orden_compra.estado_orden AS estado_orden
        FROM orden_compra
        INNER JOIN crear_pedido
            ON orden_compra.id_pedido = crear_pedido.id
        INNER JOIN proveedores
            ON orden_compra.id_proveedor = proveedores.id
        INNER JOIN detalle_producto
            ON orden_compra.cod_producto = detalle_producto.cod_producto
        """)
        return self.cursor.fetchall()

    def reporte_orden_compra(self):
        self.cursor.execute("""
        SELECT 
            orden_compra.id AS id_orden,
            orden_compra.precio_unitario AS precio_unitario,
            orden_compra.cantidad AS cantidad,
            orden_compra.fecha_orden AS fecha_orden,
            orden_compra.fecha_entrega AS fecha_entrega,
            orden_compra.estado_orden AS estado_orden,
            orden_compra.observaciones AS observaciones,
            proveedores.ID_CC_NIT AS ID_CC_NIT,
            proveedores.razon_social AS razon_social,
            proveedores.correo_electronico AS correo_electronico,
            crear_pedido.id AS id_pedido,
            crear_pedido.nombre_producto AS nombre_producto,
            crear_pedido.destino AS destino,
            crear_pedido.fecha_requerida AS fecha_requerida,
            detalle_producto.cod_producto AS cod_producto,
            detalle_producto.descripcion AS descripcion,
            detalle_producto.unidad_medida AS unidad_medida,
            detalle_producto.marca AS marca,
            detalle_producto.categoria AS categoria
        FROM orden_compra
        INNER JOIN crear_pedido
            ON orden_compra.id_pedido = crear_pedido.id
        INNER JOIN proveedores
            ON orden_compra.id_proveedor = proveedores.id
        INNER JOIN detalle_producto
            ON orden_compra.cod_producto = detalle_producto.cod_producto
        """)
        return self.cursor.fetchall()

    def obtener_pedido_para_orden(self, id_pedido):
        self.cursor.execute("""
        SELECT 
            crear_pedido.id AS id_pedido,
            crear_pedido.fecha_creacion AS fecha_creacion,
            crear_pedido.cantidad AS cantidad,
            crear_pedido.destino AS destino,
            crear_pedido.fecha_requerida AS fecha_requerida,
            crear_pedido.estado_pedido AS estado_pedido,
            usuarios.Usua_Nombre AS Usua_Nombre,
            usuarios.Usua_Correo AS Usua_Correo,
            detalle_producto.cod_producto AS cod_producto,
            detalle_producto.nombre_producto AS nombre_producto,
            detalle_producto.descripcion AS descripcion, 
            detalle_producto.unidad_medida AS unidad_medida,
            detalle_producto.precio_unitario AS precio_unitario,
            detalle_producto.categoria AS categoria,
            detalle_producto.marca AS marca
        FROM crear_pedido
        INNER JOIN usuarios
            ON crear_pedido.id_usuario = usuarios.id
        INNER JOIN detalle_producto
            ON crear_pedido.cod_producto = detalle_producto.cod_producto
        WHERE crear_pedido.id=%s
        AND crear_pedido.estado_pedido='Aprobado'      
        """ , (id_pedido,)) 
        return self.cursor.fetchone()

    def obtener_pedidos_aprobados(self):
        self.cursor.execute("""
        SELECT 
            crear_pedido.id AS id_pedido,
            usuarios.Usua_Nombre AS Usua_Nombre,
            usuarios.Usua_Correo AS correo_usuario,
            detalle_producto.cod_producto AS cod_producto,
            detalle_producto.nombre_producto AS nombre_producto,
            crear_pedido.cantidad  AS cantidad,
            crear_pedido.estado_pedido AS estado_pedido
        FROM crear_pedido
        INNER JOIN usuarios
            ON crear_pedido.id_usuario = usuarios.id
        INNER JOIN detalle_producto
            ON crear_pedido.cod_producto = detalle_producto.cod_producto
        LEFT JOIN orden_compra
            ON crear_pedido.id = orden_compra.id_pedido
        WHERE crear_pedido.estado_pedido = 'Aprobado'
        AND orden_compra.id IS NULL
    """)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()