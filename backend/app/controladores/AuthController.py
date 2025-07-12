from app.modelos.UsuarioModel import UsuarioModel

class AuthController:
    @staticmethod
    def register(data):
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return {"error": "Username y password son requeridos"}, 400

        if UsuarioModel.get_by_username(username):
            return {"error": "El usuario ya existe"}, 409

        user = UsuarioModel(username=username, password=password)
        user.create()
        return {"message": "Usuario creado correctamente"}, 201

    @staticmethod
    def login(data):
        username = data.get('username')
        password = data.get('password')
        user = UsuarioModel.get_by_username(username)
        if user and user.verify_password(password):
           return {"message": "Login exitoso", "user": user.serializar()}, 200
        return {"error": "Credenciales inválidas"}, 401

