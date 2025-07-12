from flask import Blueprint, request, jsonify
from app.controladores.AuthController import AuthController

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    return AuthController.register(data)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    return AuthController.login(data)
