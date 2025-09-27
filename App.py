from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Página base para verificar que la app corre y se renderiza correctamente
    return render_template("index.html", titulo="Sistema de Reservaciones de Consultorio Médico API", mensaje="¡Bienvenido a Sistema de Reservaciones de Consultorio Médico!")

if __name__ == "__main__":
    app.run(debug=True)