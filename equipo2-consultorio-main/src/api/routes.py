from flask import Blueprint, render_template

blueprint = Blueprint('consultorio', __name__)

@blueprint.route("/")
def home():
    """
    Renderiza la página principal del consultorio.
    """
    return render_template(
        "index.html",
        titulo="Sistema de Reservaciones de Consultorio Médico API",
        mensaje="¡Bienvenido al Sistema de Reservaciones de Consultorio Médico."
    )
