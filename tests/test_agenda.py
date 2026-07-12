import unittest
# Importamos 'agenda' en minúscula desde la carpeta 'src'
from src.agenda import agenda

class TestAgenda(unittest.TestCase):
    def setUp(self):
        # Instanciamos la clase en minúscula
        self.mi_agenda = agenda()

    def test_registro_exitoso(self):
        resultado = self.mi_agenda.registrar_contacto("Juan Perez", "0912345678")
        self.assertEqual(resultado, "Contacto 'Juan Perez' registrado exitosamente.")
        self.assertIn("Juan Perez", self.mi_agenda.contactos)
        self.assertEqual(self.mi_agenda.contactos["Juan Perez"], "0912345678")

    def test_nombre_invalido_con_numeros(self):
        with self.assertRaises(ValueError) as context:
            self.mi_agenda.registrar_contacto("Juan123", "0912345678")
        self.assertTrue("únicamente texto" in str(context.exception))

    def test_nombre_invalido_con_simbolos(self):
        with self.assertRaises(ValueError) as context:
            self.mi_agenda.registrar_contacto("Juan@Perez", "0912345678")
        self.assertTrue("únicamente texto" in str(context.exception))

    def test_telefono_invalido_letras(self):
        with self.assertRaises(ValueError) as context:
            self.mi_agenda.registrar_contacto("Maria Lopez", "091234567a")
        self.assertTrue("10 dígitos" in str(context.exception))

    def test_telefono_invalido_corto(self):
        with self.assertRaises(ValueError) as context:
            self.mi_agenda.registrar_contacto("Maria Lopez", "0912345")
        self.assertTrue("10 dígitos" in str(context.exception))

    def test_telefono_invalido_largo(self):
        with self.assertRaises(ValueError) as context:
            self.mi_agenda.registrar_contacto("Maria Lopez", "09123456789")
        self.assertTrue("10 dígitos" in str(context.exception))

if __name__ == '__main__':
    unittest.main()