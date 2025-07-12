from app.modelos.UsuarioModel import UsuarioModel

class UsuarioController:
    @staticmethod
    def login(data):
        username = data.get("username")
        password = data.get("password")
        user = UsuarioModel.validar_credenciales(username, password)
        if user:
            return {"success": True, "message": "Login exitoso", "user": user}
        else:
            return {"success": False, "message": "Credenciales inválidas"}
