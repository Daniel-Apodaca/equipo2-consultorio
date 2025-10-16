from src.extensions import db

class Paciente(db.Model):
    __tablename__ = "pacientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    contacto = db.Column(db.String(120), nullable=False)

    citas = db.relationship("Cita", back_populates="paciente")

    def __repr__(self):
        return f"Paciente(nombre={self.nombre}, edad={self.edad}, contacto={self.contacto})"
