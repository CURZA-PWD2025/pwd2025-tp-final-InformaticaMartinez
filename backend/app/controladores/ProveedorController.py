from app.modelos.ProveedorModel import ProveedorModel

class ProveedorController:
    @staticmethod
    def get_all():
        return ProveedorModel.get_all()

    @staticmethod
    def get_one(id):
        return ProveedorModel.get_one(id)

    @staticmethod
    def create(data):
        proveedor = ProveedorModel.deserializar(data)
        return proveedor.create()

    @staticmethod
    def update(data):
        proveedor = ProveedorModel.deserializar(data)
        return proveedor.update()

    @staticmethod
    def delete(id):
        return ProveedorModel.delete(id)