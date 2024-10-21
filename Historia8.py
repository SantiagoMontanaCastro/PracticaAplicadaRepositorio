import mysql.connector
from mysql.connector import Error

# Como cliente registrado, quiero poder calificar los videos que veo y consultar las calificaciones promedio de otros usuarios, para ayudar a otros clientes a elegir qué contenido ver y descubrir videos bien valorados. 



def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            user='root',
            password='1000706908',
            host='localhost',
            database='sistema_alquileres',
            port='3306'
        )
        if conexion.is_connected():
            print('Conexión exitosa a la base de datos.')
            return conexion
    except Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None



def calificar_video(conexion, id_cliente, id_pelicula, comentario='', calificacion=5):
    cursor = conexion.cursor()
    query = """
    INSERT INTO HistorialCalificaciones (ID_Cliente, ID_Pelicula, Comentario, Calificacion)
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE Comentario = %s, Calificacion = %s;
    """
    cursor.execute(query, (id_cliente, id_pelicula, comentario, calificacion, comentario, calificacion))
    conexion.commit()
    print(f'Calificación {calificacion} para el video {id_pelicula} registrada o actualizada.')


def obtener_promedio_calificaciones(conexion, id_pelicula):
    cursor = conexion.cursor()
    query = "SELECT AVG(Calificacion) FROM HistorialCalificaciones WHERE ID_Pelicula = %s;"
    cursor.execute(query, (id_pelicula,))
    promedio = cursor.fetchone()[0]
    if promedio:
        print(f'El promedio de calificaciones para la película {id_pelicula} es {promedio:.2f}.')
    else:
        print('No hay calificaciones registradas para esta película.')


def main():
    
    conexion = conectar_bd()
    if conexion is None:
        return

    
    calificar_video(conexion, id_cliente=1, id_pelicula=1, comentario='¡Me encantó!', calificacion=5)
    calificar_video(conexion, id_cliente=1, id_pelicula=2, comentario='Buena acción', calificacion=4.5)
    calificar_video(conexion, id_cliente=4, id_pelicula=1, comentario='Muy divertida', calificacion=4)

    
    obtener_promedio_calificaciones(conexion, id_pelicula=1)
    obtener_promedio_calificaciones(conexion, id_pelicula=2)

   
    conexion.close()

if __name__ == "__main__":
    main()
