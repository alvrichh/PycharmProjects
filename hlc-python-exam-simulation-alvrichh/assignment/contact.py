class Contact:
    """Representa un contacto con nombre, teléfono y email."""

    def __init__(self, nombre, telefono, email):
        """
        Inicializa un nuevo contacto.

        Args:
            nombre (str): Nombre del contacto.
            telefono (str): Número de teléfono del contacto.
            email (str): Dirección de email del contacto.
        """
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        """Devuelve la representación en cadena del contacto en formato CSV."""
        return f"{self.nombre},{self.telefono},{self.email}"

    def __eq__(self, other):
        """Compara dos contactos por su contenido."""
        if isinstance(other, Contact):
            return (self.nombre == other.nombre and
                    self.telefono == other.telefono and
                    self.email == other.email)
        return False

