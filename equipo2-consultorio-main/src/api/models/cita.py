from src.extensions import db

class Cita(db.Model):
    __tablename__ = "citas"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    motivo = db.Column(db.String(200), nullable=False)

    paciente_id = db.Column(db.Integer, db.ForeignKey("pacientes.id"))
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctores.id"))
    consultorio_id = db.Column(db.Integer, db.ForeignKey("consultorios.id"))

    paciente = db.relationship("Paciente", back_populates="citas")
    doctor = db.relationship("Doctor", back_populates="citas")
    consultorio = db.relationship("Consultorio", back_populates="citas")

    def __repr__(self):
        return (f"Cita(fecha={self.fecha}, hora={self.hora}, "
                f"paciente_id={self.paciente_id}, doctor_id={self.doctor_id}, "
                f"consultorio_id={self.consultorio_id}, motivo={self.motivo})")
