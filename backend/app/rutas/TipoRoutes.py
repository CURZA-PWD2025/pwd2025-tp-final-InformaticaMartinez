from flask import Blueprint, request, jsonify
from app.controladores.TipoController import TipoController

tipo_bp = Blueprint('tipo_bp', __name__)

@tipo_bp.route('/tipos', methods=['GET'])
def get_all():
    return jsonify(TipoController.get_all())

@tipo_bp.route('/tipos/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(TipoController.get_one(id))

@tipo_bp.route('/tipos', methods=['POST'])
def create():
    data = request.json
    return jsonify(TipoController.create(data))

@tipo_bp.route('/tipos/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    data['id'] = id
    return jsonify(TipoController.update(data))

@tipo_bp.route('/tipos/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(TipoController.delete(id))
