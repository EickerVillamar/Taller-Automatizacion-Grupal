import unittest
from src.agenda import agenda  # o Agenda, dependiendo de cómo lo guardaste
from src.busqueda_contacto import buscar_contacto

class TestRegresionAgenda(unittest.TestCase):
    def setUp(self):
        # Inicializamos un entorno limpio para la regresión
        self.mi_agenda = agenda()

    def test_regresion_reglas_de_negocio(self):
        """
        Verifica que las reglas fundamentales del negocio (solo texto, 10 dígitos)
        sigan funcionando tras las recientes integraciones del sistema.
        """
        # 1. Verificamos que la restricción de "solo texto" no se haya ro
        with self.assertRaises(ValueError) as context1:
            self.mi_agenda.registrar_contacto("Carlos123", "0991234567")
        self.assertTrue("únicamente texto" in str(context1.exception))

        # 2. Verificamos que la restricción de "10 dígitos" no se haya roto
        with self.assertRaises(ValueError) as context2:
            self.mi_agenda.registrar_contacto("Carlos Perez", "12345")
        self.assertTrue("10 dígitos" in str(context2.exception))

    def test_regresion_flujo_completo(self):
        """
        Verifica que el ciclo de vida de un contacto (registro -> almacenamiento -> búsqueda)
        se complete sin alteraciones.
        """
        # 1. Registramos un contacto válido
        mensaje_registro = self.mi_agenda.registrar_contacto("Maria Loor", "0987654321")
        self.assertEqual(mensaje_registro, "Contacto 'Maria Loor' registrado exitosamente.")

        # 2. Comprobamos que la búsqueda lo encuentra correctamente
        mensaje_busqueda = buscar_contacto(self.mi_agenda, "Maria Loor")
        self.assertEqual(mensaje_busqueda, "El número de Maria Loor es 0987654321")

if __name__ == '__main__':
    unittest.main()