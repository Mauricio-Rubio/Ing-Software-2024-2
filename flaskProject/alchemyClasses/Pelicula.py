from sqlalchemy import Column, Integer, String

from alchemyClasses import db


class Pelicula(db.Model):
    __tablename__ = 'peliculas'

    idPelicula = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45), nullable=True)
    duracion = Column(Integer, nullable=True)
    inventario = Column(Integer, nullable=False, default=1)

    def __init__(self, nombre, genero, duracion, inventario):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f"Nombre: {self.nombre}\nGénero: {self.genero}\nDuración: {self.duracion}\nInventario: {self.inventario}"