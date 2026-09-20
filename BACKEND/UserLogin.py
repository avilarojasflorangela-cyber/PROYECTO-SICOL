from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):

    def __init__(self, id, ID_CC, Usua_Nombre, Usua_Apellido, Usua_Correo, Usua_Area, contrasena):
        self.id = id
        self.ID_CC = ID_CC
        self.nombre = Usua_Nombre
        self.apellido = Usua_Apellido
        self.correo = Usua_Correo
        self.area = Usua_Area
        self.password = contrasena

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.id)
