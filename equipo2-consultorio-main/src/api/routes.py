from flask import Blueprint, render_template, jsonify
from src.api.models.paciente import Paciente
from src.api.models.doctor import Doctor
from src.api.models.consultorio import Consultorio
from src.api.models.cita import Cita

blueprint = Blueprint("consultorio", __name__)

@blueprint.route("/")
def home():
    """
    Renderiza la página principal del consultorio.
    """
    return render_template(
        "index.html",
        titulo="Sistema de Reservaciones de Consultorio Médico API",
        mensaje="¡Bienvenido al Sistema de Reservaciones de Consultorio Médico!"
    )

@blueprint.route("/pacientes", methods=["GET"])
def obtener_pacientes():
    pacientes = Paciente.query.all()
    resultado = [
        {
            "id": p.id,
            "nombre": p.nombre,
            "edad": p.edad,
            "contacto": p.contacto
        }
        for p in pacientes
    ]
    return jsonify(resultado)

@blueprint.route("/doctores", methods=["GET"])
def obtener_doctores():
    doctores = Doctor.query.all()
    resultado = [
        {
            "id": d.id,
            "nombre": d.nombre,
            "especialidad": d.especialidad,
            "consultorio_id": d.consultorio_id
        }
        for d in doctores
    ]
    return jsonify(resultado)

@blueprint.route("/consultorios", methods=["GET"])
def obtener_consultorios():
    consultorios = Consultorio.query.all()
    resultado = [
        {
            "id": c.id,
            "nombre": c.nombre,
            "direccion": c.direccion
        }
        for c in consultorios
    ]
    return jsonify(resultado)

@blueprint.route("/citas", methods=["GET"])
def obtener_citas():
    citas = Cita.query.all()
    resultado = [
        {
            "id": c.id,
            "fecha": c.fecha.isoformat(),
            "hora": c.hora.isoformat(),
            "motivo": c.motivo,
            "paciente_id": c.paciente_id,
            "doctor_id": c.doctor_id,
            "consultorio_id": c.consultorio_id
        }
        for c in citas
    ]
    return jsonify(resultado)
