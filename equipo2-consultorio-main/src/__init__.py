import os
from flask import Flask

from src.extensions import db, migrate
from src.cli import register_seed_command

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
    _register_cli(app)

    return app


def _load_config(app, config_object):
    """
    Carga configuración base y permite override por entorno.
    """
    if config_object:
        app.config.from_object(config_object)
    else:
        from src.config import Config
        app.config.from_object(Config)


def _register_blueprints(app):
    """
    Registra los blueprints principales.
    """
    from src.api.routes import blueprint as consultorio_bp
    app.register_blueprint(consultorio_bp, url_prefix="/api")


def _register_extensions(app):
    """
    Inicializa extensiones.
    """
    db.init_app(app)
    migrate.init_app(app, db)


def _register_cli(app):
    """
    Registra comandos personalizados.
    """
    register_seed_command(app)
