import os
from assignment.contact import Contact

class ContactManager:
    """Gestiona una lista de contactos y su almacenamiento en un archivo."""

    def __init__(self, filename):
        """
        Inicializa el gestor de contactos con un archivo especificado.

        Args:
            filename (str): Ruta del archivo donde se guardarán los contactos.
        """
        self.filename = filename
        self.contacts = []
        self.load_contacts()  # Cargar contactos al inicializar

    def add_contact(self, contact):
        """Agrega un nuevo contacto a la lista de contactos."""
        self.contacts.append(contact)
        self.save_contacts()

    def find_contact(self, name):

        for contact in self.contacts:
            if contact.nombre == name:
                return contact
        return None

    def save_contacts(self):
        """Guarda los contactos en el archivo especificado."""
        with open(self.filename, 'w') as file:
            for contact in self.contacts:
                file.write(str(contact) + '\n')

    def load_contacts(self):
        """Carga los contactos desde el archivo especificado."""
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                self.contacts = [Contact(*line.strip().split(',')) for line in lines]
        except IOError as e:
            raise IOError(f"No se puede cargar el archivo: {e}")
