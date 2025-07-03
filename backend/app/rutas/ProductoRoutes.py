from flask import Blueprint, request, jsonify
from app.controladores.ProductoController import ProductoController

producto_bp = Blueprint('producto_bp', __name__)

@producto_bp.route('/productos', methods=['GET'])
def get_all():
    return jsonify(ProductoController.get_all())

@producto_bp.route('/productos/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(ProductoController.get_one(id))

@producto_bp.route('/productos', methods=['POST'])
def create():
    data = request.json
    return jsonify(ProductoController.create(data))

@producto_bp.route('/productos/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    data['id'] = id
    return jsonify(ProductoController.update(data))

@producto_bp.route('/productos/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(ProductoController.delete(id))
