from app.modelos.TipoModel import TipoModel

class TipoController:
    @staticmethod
    def get_all():
        return TipoModel.get_all()

    @staticmethod
    def get_one(id):
        return TipoModel.get_one(id)

    @staticmethod
    def create(data):
        tipo = TipoModel.deserializar(data)
        return tipo.create()

    @staticmethod
    def update(data):
        tipo = TipoModel.deserializar(data)
        return tipo.update()

    @staticmethod
    def delete(id):
        return TipoModel.delete(id)