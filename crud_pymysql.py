from datetime import datetime, timedelta
import pymysql


def change_movie_genre(con, movie_name, new_genre):
    try:
        with con.cursor() as cr:
            cr.execute(
                "SELECT idPelicula FROM peliculas WHERE nombre = %s", (movie_name,)
            )
            movies = cr.fetchall()

            if not movies:
                print(f"Movie '{movie_name}' does not exist.")
                return
            for movie in movies:
                cr.execute(
                    "UPDATE peliculas SET genero = %s WHERE idPelicula = %s",
                    (new_genre, movie[0]),
                )
                print(
                    f"Genre of movie '{movie_name}' has been changed to '{new_genre}'"
                )
                con.commit()

    finally:
        con.commit()


def insert_rental_record(con, usuario_data, pelicula_data, rentar_data):
    try:
        with con.cursor() as cr:
            cr.execute(
                "INSERT INTO usuarios (nombre, password, apPat, apMat, email) VALUES (%s, %s, %s, %s, %s)",
                usuario_data,
            )
            usuario_id = cr.lastrowid
            cr.execute(
                "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)",
                pelicula_data,
            )
            pelicula_id = cr.lastrowid
            cr.execute(
                "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)",
                (
                    usuario_id,
                    pelicula_id,
                    rentar_data[0],
                    rentar_data[1],
                    rentar_data[2],
                ),
            )

    finally:
        con.commit()


def filter_users_by_last_name_ending(con, end_string):
    try:
        with con.cursor() as cr:
            query = (
                "SELECT * FROM usuarios WHERE apPat LIKE %s OR apMat LIKE %s"
            )
            cr.execute(query, ("%" + end_string + "%", "%" + end_string + "%"))
            users = cr.fetchall()
            for user in users:
                print(user)
    finally:
        pass


def remove_old_rents(con):

    try:
        with con.cursor() as cr:
            three_days_ago = datetime.now() - timedelta(days=3)
            formatted_date = three_days_ago.strftime("%Y-%m-%d %H:%M:%S")
            cr.execute("DELETE FROM rentar WHERE fecha_renta <= %s", (formatted_date,))
            print(f"Removed old rents prior to {formatted_date}")

    finally:
        con.commit()


def main():
    connection = pymysql.connect(
        host="localhost",
        user="tester",
        password="Llm)I)mCC1lq(Ti@",
        database="lab_ing_software",
    )
    data_list = [
        {
            "usuario_data": (
                "John",
                "password123",
                "Doe",
                "Williams",
                "john@example.com",
            ),
            "pelicula_data": ("Movie Name", "Action", 120, 5),
            "rentar_data": ("2024-02-18", 7, 0),
        },
        {
            "usuario_data": (
                "Mauricio",
                "password123",
                "Gonzalez",
                "Ramos",
                "mau@example.com",
            ),
            "pelicula_data": ("Pulp fiction", "Noir", 120, 1),
            "rentar_data": ("2024-02-21", 3, 1),
        },
        {
            "usuario_data": (
                "Ruben",
                "password123",
                "Gonzalez",
                "Ramos",
                "rub@example.com",
            ),
            "pelicula_data": ("Django", "Western", 190, 2),
            "rentar_data": ("2024-02-11", 0, 2),
        },
        {
            "usuario_data": (
                "Oscar",
                "password123",
                "Gonzalez",
                "Ramos",
                "osc@example.com",
            ),
            "pelicula_data": ("Kill Bill", "Action", 120, 3),
            "rentar_data": ("2024-02-11", 0, 2),
        },
    ]

    for data in data_list:
        insert_rental_record(
            connection,
            data["usuario_data"],
            data["pelicula_data"],
            data["rentar_data"],
        )

    end_string = input("Enter the ending of the last name: ")
    filter_users_by_last_name_ending(connection, end_string)

    change_movie_genre(connection, "Kill Bill", "Noir")
    change_movie_genre(connection, "Lorem", "Noir")
    remove_old_rents(connection)
    connection.close()


if __name__ == "__main__":
    main()
