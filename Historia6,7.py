import mysql.connector
import getpass
import random
import string
import hashlib

# Como cliente registrado, quiero poder ver una opción para mostrar u ocultar la contraseña mientras la escribo, para asegurarme de que la estoy ingresando correctamente. 
# Como cliente registrado, quiero poder recuperar mi contraseña si la olvido, para poder restablecer mi acceso a la cuenta. 


conexion = mysql.connector.connect(
    user='root', 
    password='1000706908', 
    host='localhost', 
    database='sistema_alquileres', 
    port='3306'
)


if conexion.is_connected():
    print("Conexión exitosa a la base de datos")


def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()


def registrar_cliente(nombre, apellido, correo, contraseña):
    cursor = conexion.cursor()
    query = """
        INSERT INTO Cliente (Nombre, Apellido, CorreoElectronico, Contraseña) 
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (nombre, apellido, correo, encriptar_contraseña(contraseña)))
    conexion.commit()
    cursor.close()


def obtener_contraseña(correo):
    cursor = conexion.cursor()
    query = "SELECT Contraseña FROM Cliente WHERE CorreoElectronico = %s"
    cursor.execute(query, (correo,))
    resultado = cursor.fetchone()
    cursor.close()
    return resultado[0] if resultado else None


def iniciar_sesion():
    email = input("Ingresa tu correo electrónico: ")

    
    contraseña_en_bd = obtener_contraseña(email)
    if contraseña_en_bd is None:
        print("Este correo no está registrado.")
        return False

    
    while True:
        mostrar = input("¿Deseas mostrar la contraseña mientras la escribes? (s/n): ").lower() == 's'
        password = solicitar_contraseña(mostrar)
        if encriptar_contraseña(password) == contraseña_en_bd:
            print("¡Inicio de sesión exitoso!")
            return True
        else:
            print("Contraseña incorrecta. Inténtalo de nuevo.")


def solicitar_contraseña(mostrar=False):
    if mostrar:
        return input("Contraseña: ")
    else:
        return getpass.getpass("Contraseña (oculta): ")


def recuperar_contraseña():
    email = input("Ingresa tu correo electrónico para recuperar la contraseña: ")

    
    contraseña_en_bd = obtener_contraseña(email)
    if contraseña_en_bd is None:
        print("Este correo no está registrado.")
        return


    enlace = generar_enlace_recuperacion()
    print(f"Hemos enviado un enlace para restablecer tu contraseña: {enlace}")
    print("Este enlace expira en 24 horas.")


def generar_enlace_recuperacion():
    
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    return f"http://ejemplo.com/reset?token={token}"


def menu_principal():
    while True:
        print("\n--- Menú ---")
        print("1. Iniciar sesión")
        print("2. ¿Olvidaste tu contraseña?")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            iniciar_sesion()
        elif opcion == '2':
            recuperar_contraseña()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu_principal()
