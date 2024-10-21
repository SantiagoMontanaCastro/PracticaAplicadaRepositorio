import mysql.connector
from datetime import datetime, timedelta

#Como cliente, quiero poder alquilar videos en línea con restricciones de tiempo o de número de reproducciones, para disfrutar del contenido de acuerdo con mis preferencias y necesidades. 



def conectar_bd():
    return mysql.connector.connect(
        user='root',
        password='1000706908',
        host='localhost',
        database='sistema_alquileres',
        port='3306'
    )


def alquilar_video(conexion, id_pelicula, id_cliente, dias_alquiler=30):
    cursor = conexion.cursor()
    fecha_alquiler = datetime.now()
    fecha_expiracion = fecha_alquiler + timedelta(days=dias_alquiler)

    query = """
    INSERT INTO Alquiler (ID_Pelicula, FechaAlquiler, FechaExpiracion)
    VALUES (%s, %s, %s);
    """
    cursor.execute(query, (id_pelicula, fecha_alquiler, fecha_expiracion))
    conexion.commit()
    print(f'Película {id_pelicula} alquilada hasta {fecha_expiracion.date()} por el cliente {id_cliente}.')


def consultar_tiempo_restante(conexion, id_pelicula):
    cursor = conexion.cursor()
    query = "SELECT FechaExpiracion FROM Alquiler WHERE ID_Pelicula = %s;"
    cursor.execute(query, (id_pelicula,))
    fecha_expiracion = cursor.fetchone()
    
    if fecha_expiracion:
        
        if isinstance(fecha_expiracion[0], datetime):
            tiempo_restante = fecha_expiracion[0] - datetime.now()
        else:
            
            fecha_expiracion_datetime = datetime.combine(fecha_expiracion[0], datetime.min.time())
            tiempo_restante = fecha_expiracion_datetime - datetime.now()
        
        if tiempo_restante.total_seconds() > 0:
            print(f'Tiempo restante: {tiempo_restante}.')
        else:
            print('El alquiler ha expirado.')
    else:
        print('No se encontró registro de alquiler.')


def main():
   
    conexion = conectar_bd()
    
    
    alquilar_video(conexion, id_pelicula=1, id_cliente=1, dias_alquiler=30)

    
    consultar_tiempo_restante(conexion, id_pelicula=1)

    
    conexion.close()

if __name__ == "__main__":
    main()
