from src.extensions import db

class Doctor(db.Model):
    __tablename__ = "doctores"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    especialidad = db.Column(db.String(120), nullable=False)

    consultorio_id = db.Column(db.Integer, db.ForeignKey("consultorios.id"))
    consultorio = db.relationship("Consultorio", back_populates="doctores")

    citas = db.relationship("Cita", back_populates="doctor")

    def __repr__(self):
        return f"Doctor(nombre={self.nombre}, especialidad={self.especialidad})"

