import unittest
from src.agenda import agenda # o agenda, dependiendo de tu versión final
from src.busqueda_contacto import buscar_contacto

class TestIntegracionAgenda(unittest.TestCase):
    def test_registro_y_busqueda_integrados(self):
        # 1. Instanciamos la agenda
        mi_agenda = agenda()

        # 2. Usamos el módulo de registro
        mi_agenda.registrar_contacto("Ana Gomez", "0987654321")

        # 3. Usamos el módulo de búsqueda para verificar que la información fluyó correctamente
        resultado_busqueda = buscar_contacto(mi_agenda, "Ana Gomez")

        # 4. Validamos la integración
        self.assertEqual(resultado_busqueda, "El número de Ana Gomez es 0987654321")