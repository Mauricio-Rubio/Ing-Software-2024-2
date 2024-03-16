from sqlalchemy import Column, Integer, String

from alchemyClasses import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    apPat = Column(String(200), nullable=False)
    apMat = Column(String(200))
    password = Column(String(64), nullable=False)
    email = Column(String(500))
    profilePicture = Column(String(500))
    superUser = Column(Integer)

    def __init__(self, nombre, apPat, apMat, password, email, profilePicture, superUser):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser

    def __str__(self):
        return f"ID Usuario: {self.idUsuario}\nNombre: {self.nombre}\nApellido Paterno: {self.apPat}\nApellido Materno: {self.apMat}\nContraseña: {self.password}\nEmail: {self.email}\nProfile Picture: {self.profilePicture}\nSuper User: {self.superUser}"