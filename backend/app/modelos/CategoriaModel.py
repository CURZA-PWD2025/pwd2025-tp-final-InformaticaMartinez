from app.conexion import get_connection

class CategoriaModel:
    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {"id": self.id, "nombre": self.nombre}

    @staticmethod
    def deserializar(data):
        return CategoriaModel(id=data.get("id"), nombre=data.get("nombre"))

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categorias")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    @staticmethod
    def get_one(id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categorias WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    def create(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categorias (nombre) VALUES (%s)", (self.nombre,))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def update(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE categorias SET nombre=%s WHERE id=%s", (self.nombre, self.id))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    @staticmethod
    def delete(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categorias WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True