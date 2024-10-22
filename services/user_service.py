from repositories.user_repository import UserRepository
from models import User

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def listar_usuarios(self):
        return self.repository.get_all()

    def crear_usuario(self, username, password, role='user'):
        nuevo_usuario = User(username=username, role=role)
        nuevo_usuario.set_password(password)
        self.repository.add(nuevo_usuario)

    def editar_usuario(self, user_id, username, password=None, role=None):
        usuario = self.repository.get_by_id(user_id)
        if usuario:
            usuario.username = username
            if password:
                usuario.set_password(password)
            if role:
                usuario.role = role
            self.repository.update()

    def eliminar_usuario(self, user_id):
        usuario = self.repository.get_by_id(user_id)
        if usuario:
            self.repository.delete(usuario)

    def verificar_usuario(self, username, password):
        usuario = User.query.filter_by(username=username).first()
        if usuario and usuario.check_password(password):
            return usuario
        return None
