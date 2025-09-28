class Consultorio:
    def __init__(self, nombre, direccion, doctores=None):
        self.nombre = nombre
        self.direccion = direccion
        self.doctores = doctores if doctores else []

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def __repr__(self):
        return f"Consultorio(nombre={self.nombre}, direccion={self.direccion})"
