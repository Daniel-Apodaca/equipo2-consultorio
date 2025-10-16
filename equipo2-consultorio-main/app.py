#punto de entrada que usa create_app() como punto de entrada
from src import create_app
from flask import render_template


app = create_app("src.config.DevelopmentConfig")

@app.route("/")
def home():
    return render_template(
        "index.html",
        titulo="Sistema de Reservaciones de Consultorio Médico API",
        mensaje="¡Bienvenido al Sistema de Reservaciones de Consultorio Médico!"
    )