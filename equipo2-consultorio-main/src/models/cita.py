class Cita:
    def __init__(self, fecha, hora, paciente, doctor, consultorio, motivo):
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.doctor = doctor
        self.consultorio = consultorio
        self.motivo = motivo

    def __repr__(self):
        return (f"Cita(fecha={self.fecha}, hora={self.hora}, "
                f"paciente={self.paciente.nombre}, doctor={self.doctor.nombre}, "
                f"consultorio={self.consultorio.nombre}, motivo={self.motivo})")
