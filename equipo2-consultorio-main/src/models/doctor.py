class Doctor:
    def __init__(self, nombre, especialidad, horarios_disponibles=None):
        self.nombre = nombre
        self.especialidad = especialidad
        self.horarios_disponibles = horarios_disponibles if horarios_disponibles else []

    def __repr__(self):
        return f"Doctor(nombre={self.nombre}, especialidad={self.especialidad})"
