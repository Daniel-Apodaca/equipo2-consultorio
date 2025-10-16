from src.extensions import db

class Consultorio(db.Model):
    __tablename__ = "consultorios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)

    doctores = db.relationship("Doctor", back_populates="consultorio")
    citas = db.relationship("Cita", back_populates="consultorio")

    def __repr__(self):
        return f"Consultorio(nombre={self.nombre}, direccion={self.direccion})"
