from app.conexion import get_connection
import hashlib

class UsuarioModel:
    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password

    def serializar(self):
        return {"id": self.id, "username": self.username}

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def validar_credenciales(username, password):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        hashed_password = UsuarioModel.hash_password(password)
        cursor.execute("SELECT * FROM usuarios WHERE username=%s AND password=%s", (username, hashed_password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user
