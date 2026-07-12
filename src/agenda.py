

import re

class agenda:
    def __init__(self):
        # Diccionario para almacenar los contactos {nombre: telefono}
        self.contactos = {}

    def registrar_contacto(self, nombre: str, telefono: str) -> str:
        # Validación 1: El nombre debe corresponder únicamente a texto (permite espacios)
        if not re.fullmatch(r'[A-Za-zÁ-Úá-úñÑ\s]+', nombre):
            raise ValueError("Error: El nombre debe contener únicamente texto.")

        # Validación 2: El teléfono debe tener exactamente 10 dígitos numéricos
        if not re.fullmatch(r'\d{10}', telefono):
            raise ValueError("Error: El número telefónico debe tener exactamente 10 dígitos.")
        # Registrar el contacto
        self.contactos[nombre] = telefono
        return f"Contacto '{nombre}' registrado exitosamente."

