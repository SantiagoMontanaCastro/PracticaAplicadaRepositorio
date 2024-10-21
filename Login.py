import re 
from datetime import datetime, timedelta

# Simulación de una base de datos de usuarios
usuarios_registrados = {}

# Clase para gestionar el sistema de usuarios
class SistemaDeUsuarios:
    
    def __init__(self):
        self.reset_tokens = {}

    # Registro de usuario
    def registrar_usuario(self, email, password):
        if self.validar_email(email):
            if email in usuarios_registrados:
                return "El correo electrónico ya está registrado. Por favor, intente iniciar sesión."
            if not self.validar_password(password):
                return "La contraseña no cumple con los criterios de seguridad establecidos."
            # Guardar el usuario
            usuarios_registrados[email] = password
            self.enviar_correo_confirmacion(email)
            return "Registro completado con éxito. Por favor, revisa tu correo electrónico para confirmar tu cuenta."
        else:
            return "La dirección de correo electrónico ingresada no es válida."

    # Validar formato de email
    def validar_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    # Validar contraseña segura
    def validar_password(self, password):
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'\d', password):
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        return True

    # Simulación de envío de correo de confirmación
    def enviar_correo_confirmacion(self, email):
        print(f"Se ha enviado un correo de confirmación a la dirección: {email}.")

    # Recuperar contraseña
    def recuperar_password(self, email):
        if email not in usuarios_registrados:
            return "El correo electrónico es incorrecto o no está registrado. Por favor, inténtelo de nuevo."
            
        token = self.generar_token_recuperacion(email)
        self.reset_tokens[email] = {'token': token, 'expira': datetime.now() + timedelta(hours=24)}
        self.enviar_correo_recuperacion(email, token)
        return "Se ha enviado un correo con el enlace de recuperación."

    # Generar token de recuperación (simulado)
    def generar_token_recuperacion(self, email):
        return f"token-{email}"

    # Simulación de envío de correo de recuperación
    def enviar_correo_recuperacion(self, email, token):
        print(f"Se ha enviado un enlace de recuperación a {email}. Código de recuperación: {token}")

    # Verificar token de recuperación
    def verificar_token_recuperacion(self, email, token):
        if email in self.reset_tokens:
            datos_token = self.reset_tokens[email]
            if datos_token['token'] == token and datos_token['expira'] > datetime.now():
                return True
        return False

    # Restablecer contraseña con un token válido
    def restablecer_password(self, email, token, nueva_password):
        if self.verificar_token_recuperacion(email, token):
            if self.validar_password(nueva_password):
                usuarios_registrados[email] = nueva_password
                del self.reset_tokens[email]
                return "Contraseña restablecida con éxito."
            else:
                return "La nueva contraseña no cumple con los requisitos de seguridad."
        else:
            return "Enlace de recuperación inválido o expirado."

    # Iniciar sesión
    def iniciar_sesion(self, email, password):
        if email not in usuarios_registrados:
            return "Correo electrónico no registrado, porfavor intente nuevamente."
        if usuarios_registrados[email] != password:
            return "Contraseña incorrecta. Intente nuevamente con una contraseña más segura."
        return "Inicio de sesión exitoso."

# Función principal que solicita los datos al usuario
def main():
    sistema = SistemaDeUsuarios()

    while True:
        print("\nBienvenido al sistema de gestión de usuarios.")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Recuperar contraseña")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            email = input("Introduce tu correo electrónico: ")
            password = input("Introduce tu contraseña: ")
            try:
                resultado = sistema.iniciar_sesion(email, password)
                print(resultado)
                if resultado == "Inicio de sesión exitoso.":
                    break  # Salir del bucle si el inicio de sesión es exitoso
            
            except Exception as e:
                print(f"Error: {e}. Intente nuevamente.")
        
        elif opcion == "2":
            email = input("Introduce tu correo electrónico: ")
            password = input("Introduce tu contraseña (debe contener caracteres hexadecimales y al menos un carácter especial): ")

            print(sistema.registrar_usuario(email, password))
        
        elif opcion == "3":
            email = input("Introduce tu correo electrónico para recuperar la contraseña: ")
            print(sistema.recuperar_password(email))
        
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()  