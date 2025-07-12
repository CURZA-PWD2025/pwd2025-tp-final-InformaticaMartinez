from flask import Blueprint, request, jsonify
from app.controladores.UsuarioController import UsuarioController

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    return jsonify(UsuarioController.login(data))
