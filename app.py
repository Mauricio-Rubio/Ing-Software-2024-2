from flask import Flask
from alchemyClasses import db

from model.model_pelicula import *
from model.model_usuario import *
from model.model_renta import *

app = Flask(__name__)
password = "Llm)I)mCC1lq(Ti@"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://tester:{}@localhost:3306/lab_ing_software".format(password.replace("@", "%40"))
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():

####################################################################
        for usuario in get_all_usuarios():
            print(usuario)

        for pelicula in get_all_peliculas():
            print(pelicula)

        for renta in get_all_rentas():
            print(renta)
# ####################################################################
        print(search_pelicula_by_id(1))
        print(search_pelicula_by_id(2))
        print(search_pelicula_by_id(3))
        print(search_usuario_by_id(1))
        print(search_usuario_by_id(15))
        print(search_renta_by_id(2))
        print(search_renta_by_id(3))
# ####################################################################
        
        print(update_pelicula_by_id(1, nombre="La vita e bella", duracion=190))
        print(update_pelicula_by_id(2, nombre="Seventh Seal", duracion=120, genero="Drama", inventario=10))
        print(update_usuario_by_id(14, nombre="Fernando", email="fer@gmail.com", profilePicture="fer.jpg"))
        print(update_renta_by_id(2, fecha_renta="2021-10-10", dias_de_renta="10", idPelicula=2, idUsuario=14))

####################################################################
        
        print(del_pelicula_by_id(2), all=True)
        print(del_usuario_by_id(14))
        print(del_renta_by_id(2))

####################################################################