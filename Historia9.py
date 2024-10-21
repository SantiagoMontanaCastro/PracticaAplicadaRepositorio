import mysql.connector

# Como usuario del sistema de gestión de contenido, quiero poder registrar y actualizar las categorías de los videos (como comedia, terror, acción), para facilitar la búsqueda y filtrado de contenido según el género. 




def conectar_bd():
    return mysql.connector.connect(
        user='root',
        password='1000706908',
        host='localhost',
        database='sistema_alquileres',
        port='3306'
    )



def registrar_categoria(conexion, nombre_categoria):
    cursor = conexion.cursor()
    query = "INSERT INTO Categoria (Nombre) VALUES (%s);"
    cursor.execute(query, (nombre_categoria,))
    conexion.commit()
    print(f'Categoría "{nombre_categoria}" registrada con éxito.')




def actualizar_categoria(conexion, id_categoria, nuevo_nombre):
    cursor = conexion.cursor()
    query = "UPDATE Categoria SET Nombre = %s WHERE ID_Categoria = %s;"
    cursor.execute(query, (nuevo_nombre, id_categoria))
    conexion.commit()
    print(f'Categoría actualizada a "{nuevo_nombre}".')




def main():
   
    conexion = conectar_bd()

  
    registrar_categoria(conexion, nombre_categoria='Comedia')
    registrar_categoria(conexion, nombre_categoria='Terror')
    registrar_categoria(conexion, nombre_categoria='Acción')

  
    actualizar_categoria(conexion, id_categoria=1,
                         nuevo_nombre='Comedia Romántica')

  
    conexion.close()


if __name__ == "__main__":
    main()
