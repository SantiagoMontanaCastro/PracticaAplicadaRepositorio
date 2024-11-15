import unittest
from unittest.mock import patch, MagicMock
import hashlib
from Historia6 import encriptar_contraseña, registrar_cliente, obtener_contraseña, iniciar_sesion, recuperar_contraseña, generar_enlace_recuperacion

class TestSistemaAlquileres(unittest.TestCase):
    
    def test_encriptar_contraseña(self):
        
        contraseña = "mi_password_seguro"
        resultado = encriptar_contraseña(contraseña)
        self.assertEqual(resultado, hashlib.sha256(contraseña.encode()).hexdigest())
    
    @patch('Historia6.conexion')
    def test_registrar_cliente(self, mock_conexion):
        
        mock_cursor = MagicMock()
        mock_conexion.cursor.return_value = mock_cursor

       
        registrar_cliente('Juan', 'Pérez', 'juan@example.com', 'password123')
        
       
        mock_cursor.execute.assert_called_with(
            "INSERT INTO Cliente (Nombre, Apellido, CorreoElectronico, Contraseña) VALUES (%s, %s, %s, %s)",
            ('Juan', 'Pérez', 'juan@example.com', encriptar_contraseña('password123'))
        )
        
        mock_conexion.commit.assert_called_once()
    
    @patch('Historia6.obtener_contraseña')
    def test_iniciar_sesion_contraseña_correcta(self, mock_obtener_contraseña):
       
        mock_obtener_contraseña.return_value = encriptar_contraseña('password_correcta')

       
        with patch('builtins.input', side_effect=['usuario@example.com', 'n', 'password_correcta']):
            with patch('Historia6.getpass.getpass', return_value='password_correcta'):
                resultado = iniciar_sesion()
                self.assertTrue(resultado)
    
    @patch('Historia6.obtener_contraseña')
    def test_iniciar_sesion_contraseña_incorrecta(self, mock_obtener_contraseña):
        
        mock_obtener_contraseña.return_value = encriptar_contraseña('password_correcta')

       
        with patch('builtins.input', side_effect=['usuario@example.com', 'n', 'password_incorrecta']):
            with patch('Historia6.getpass.getpass', return_value='password_incorrecta'):
                resultado = iniciar_sesion()
                self.assertFalse(resultado)

    @patch('Historia6.obtener_contraseña')
    def test_recuperar_contraseña_usuario_no_registrado(self, mock_obtener_contraseña):
       
        mock_obtener_contraseña.return_value = None

        with patch('builtins.input', return_value='no_registrado@example.com'):
            recuperar_contraseña()

       
        mock_obtener_contraseña.assert_called_with('no_registrado@example.com')
    
    def test_generar_enlace_recuperacion(self):
       
        enlace = generar_enlace_recuperacion()
        self.assertTrue(enlace.startswith("http://ejemplo.com/reset?token="))
        self.assertEqual(len(enlace.split('=')[-1]), 20)


if __name__ == '__main__':
    unittest.main()
