from click import echo
from datetime import date, time

from src.extensions import db
from src.api.models.paciente import Paciente
from src.api.models.doctor import Doctor
from src.api.models.consultorio import Consultorio
from src.api.models.cita import Cita

def register_seed_command(app):
    @app.cli.command("seed")
    def seed():
        if Paciente.query.first():
            echo("Seed already applied.")
            return

        # Crear paciente
        paciente = Paciente(
            nombre="Daniel Apodaca",
            edad=30,
            contacto="daniel@example.com"
        )

        # Crear consultorio
        consultorio = Consultorio(
            nombre="Consultorio Central",
            direccion="Av. Revolución 123, Tijuana"
        )

        # Crear doctor
        doctor = Doctor(
            nombre="Dra. Ana López",
            especialidad="Medicina General",
            consultorio=consultorio
        )

        # Crear cita
        cita = Cita(
            fecha=date.today(),
            hora=time(10, 30),
            motivo="Consulta general",
            paciente=paciente,
            doctor=doctor,
            consultorio=consultorio
        )

        # Agregar todo a la sesión
        db.session.add_all([paciente, consultorio, doctor, cita])
        db.session.commit()

        echo("Seed completed: paciente, doctor, consultorio y cita creados.")
