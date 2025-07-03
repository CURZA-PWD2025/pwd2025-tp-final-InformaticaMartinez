from flask import Flask
from flask_cors import CORS

from app.rutas.ProductoRoutes import producto_bp
from app.rutas.TipoRoutes import tipo_bp
from app.rutas.CategoriaRoutes import categoria_bp
from app.rutas.ProveedorRoutes import proveedor_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(producto_bp)
    app.register_blueprint(tipo_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(proveedor_bp)

    @app.route('/')
    def index():
        return '<h1>Sistema de Cervecería funcionando 🍺</h1>'

    return app