from Conexionbasededatos import ConexionMysql
class Model_ConsultarEstado:
    def __init__(self):
        self.mibasededatos = ConexionMysql()
        self.conexion = self.mibasededatos.conexion 
        self.cursor = self.mibasededatos.cursor

    def consultar_estado(self, id_pedido):
        self.cursor.execute("""
        SELECT 
            crear_pedido.id AS id_pedido,
            usuarios.Usua_Nombre AS Usua_Nombre,
            crear_pedido.estado_pedido AS estado_pedido,
            orden_compra.id AS id_orden,
            proveedores.razon_social AS razon_social,
            detalle_producto.cod_producto AS cod_producto,
            detalle_producto.nombre_producto AS nombre_producto,
            facturas.id AS id_factura,
            facturas.estado_factura AS estado_factura
        FROM crear_pedido
        INNER JOIN usuarios
            ON crear_pedido.id_usuario = usuarios.id
        LEFT JOIN orden_compra
            ON crear_pedido.id = orden_compra.id_pedido
        LEFT JOIN proveedores
            ON orden_compra.id_proveedor = proveedores.id
        LEFT JOIN detalle_producto
            ON orden_compra.cod_producto = detalle_producto.cod_producto
        LEFT JOIN facturas
            ON orden_compra.id = facturas.id_orden
        WHERE crear_pedido.id=%s
        """, (id_pedido,))
        return self.cursor.fetchone()
