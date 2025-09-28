class Paciente:
    def __init__(self, nombre, edad, contacto):
        self.nombre = nombre
        self.edad = edad
        self.contacto = contacto

    def __repr__(self):
        return f"Paciente(nombre={self.nombre}, edad={self.edad}, contacto={self.contacto})"
