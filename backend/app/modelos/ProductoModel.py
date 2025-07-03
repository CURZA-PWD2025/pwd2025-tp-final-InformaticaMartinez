from app.conexion import get_connection

class ProductoModel:
    def __init__(self, id=None, nombre=None, precio=None, tipo_id=None, categoria_id=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.tipo_id = tipo_id
        self.categoria_id = categoria_id

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "tipo_id": self.tipo_id,
            "categoria_id": self.categoria_id,
        }

    @staticmethod
    def deserializar(data):
        return ProductoModel(
            id=data.get("id"),
            nombre=data.get("nombre"),
            precio=data.get("precio"),
            tipo_id=data.get("tipo_id"),
            categoria_id=data.get("categoria_id")
        )

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.id, p.nombre, p.precio,
                   t.nombre AS tipo_nombre,
                   c.nombre AS categoria_nombre
            FROM productos p
            JOIN tipos t ON p.tipo_id = t.id
            JOIN categorias c ON p.categoria_id = c.id
        """)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    @staticmethod
    def get_one(id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    def create(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO productos (nombre, precio, tipo_id, categoria_id)
            VALUES (%s, %s, %s, %s)
        """, (self.nombre, self.precio, self.tipo_id, self.categoria_id))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def update(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE productos
            SET nombre=%s, precio=%s, tipo_id=%s, categoria_id=%s
            WHERE id=%s
        """, (self.nombre, self.precio, self.tipo_id, self.categoria_id, self.id))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    @staticmethod
    def delete(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
