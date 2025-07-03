from app.modelos.ProductoModel import ProductoModel

class ProductoController:
    @staticmethod
    def get_all():
        return ProductoModel.get_all()

    @staticmethod
    def get_one(id):
        return ProductoModel.get_one(id)

    @staticmethod
    def create(data):
        producto = ProductoModel.deserializar(data)
        return producto.create()

    @staticmethod
    def update(data):
        producto = ProductoModel.deserializar(data)
        return producto.update()

    @staticmethod
    def delete(id):
        return ProductoModel.delete(id)
