def buscar_contacto(instancia_agenda, nombre: str) -> str:
    """
    Busca un contacto dentro de la instancia de la agenda proporcionada.
    """
    # Verifica si el nombre existe como llave en el diccionario de la agenda
    if nombre in instancia_agenda.contactos:
        return f"El número de {nombre} es {instancia_agenda.contactos[nombre]}"
    else:
        raise ValueError(f"Error: El contacto '{nombre}' no fue encontrado.")