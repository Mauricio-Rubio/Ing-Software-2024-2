from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from alchemyClasses import db


class Renta(db.Model):
    __tablename__ = 'rentar'

    idRentar = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Boolean, default=False)

    pelicula = relationship('Pelicula', backref='rentas')
    usuario = relationship('Usuario', backref='rentas')

    def __init__(self, idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return f"ID Usuario: {self.idUsuario}\nID Película: {self.idPelicula}\nFecha de renta: {self.fecha_renta}\nDías de renta: {self.dias_de_renta}\n Entregada: {self.estatus}"