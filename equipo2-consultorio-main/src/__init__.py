from flask import Flask

import os
from flask import Flask

def create_app(config_object=None):
    """
    Crea y configura la instancia principal de Flask.
    """
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "..", "templates")
    )

    _load_config(app, config_object)
    _register_blueprints(app)
    _register_extensions(app)
    return app


def _load_config(app, config_object):
    """
    Carga configuración base y permite override por entorno.

    Args:
        app (Flask): La instancia de la aplicación.
        config_object (str | None): Ruta al objeto de configuración opcional.
    """
    if config_object:
        app.config.from_object(config_object)
    else:
        from src.config import Config
        app.config.from_object(Config)

def _register_blueprints(app):
    """
    Registra los blueprints principales.

    Args:
        app (Flask): La instancia de la aplicación.
    """
    from src.api.routes import blueprint as consultorio_bp
    app.register_blueprint(consultorio_bp)

def _register_extensions(app):
    """
    Inicializa extensiones (placeholder).

    Args:
        app (Flask): La instancia de la aplicación.
    """
    pass
