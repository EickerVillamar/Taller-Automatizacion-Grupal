import unittest
from unittest.mock import patch
import io
import sys

# Importamos la función principal de nuestra app
from app import iniciar_aplicacion

class TestE2EAgenda(unittest.TestCase):
    
    # patch simula los inputs del usuario en el orden exacto en que la app los pedirá
    @patch('builtins.input', side_effect=[
        '1', 'Lucia Viteri', '0991122334',  # Flujo 1: Selecciona opción 1, ingresa nombre, ingresa teléfono
        '2', 'Lucia Viteri',                # Flujo 2: Selecciona opción 2, ingresa nombre a buscar
        '3'                                 # Flujo 3: Selecciona opción 3 para salir
    ])
    def test_flujo_completo_usuario(self, mock_input):
        """
        Prueba E2E: Simula a un usuario abriendo la app, registrando un contacto, 
        buscándolo y luego saliendo de la aplicación.
        """
        # Redirigimos la salida de la consola (los prints) para poder leerlos en la prueba
        salida_consola = io.StringIO()
        sys.stdout = salida_consola

        # Ejecutamos la aplicación
        iniciar_aplicacion()

        # Restauramos la salida normal de la consola
        sys.stdout = sys.__stdout__

        # Obtenemos todo el texto que la aplicación imprimió en pantalla
        resultado_impreso = salida_consola.getvalue()

        # Verificamos visualmente (en el texto capturado) que el usuario vio el éxito del proceso
        self.assertIn("Contacto 'Lucia Viteri' registrado exitosamente.", resultado_impreso)
        self.assertIn("El número de Lucia Viteri es 0991122334", resultado_impreso)
        self.assertIn("Saliendo de la agenda...", resultado_impreso)

if __name__ == '__main__':
    unittest.main()
