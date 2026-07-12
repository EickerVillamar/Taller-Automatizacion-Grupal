import unittest
# Importamos la agenda y la función de búsqueda
from src.agenda import agenda
from src.busqueda_contacto import buscar_contacto

class TestBusquedaContacto(unittest.TestCase):
    def setUp(self):
        # Preparamos una agenda con un contacto de prueba
        self.mi_agenda = agenda()
        self.mi_agenda.registrar_contacto("Pedro Lopez", "0998877665")

    def test_busqueda_exitosa(self):
        # Probamos buscar el contacto que acabamos de registrar
        resultado = buscar_contacto(self.mi_agenda, "Pedro Lopez")
        self.assertEqual(resultado, "El número de Pedro Lopez es 0998877665")

    def test_busqueda_fallida_no_existe(self):
        # Probamos buscar un contacto que no existe
        with self.assertRaises(ValueError) as context:
            buscar_contacto(self.mi_agenda, "Alguien Desconocido")
        self.assertTrue("no fue encontrado" in str(context.exception))

if __name__ == '__main__':
    unittest.main()