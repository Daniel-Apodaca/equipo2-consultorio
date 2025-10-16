class Config:
    """
    Configuración base para la aplicación Flask.
    """
    SECRET_KEY = "dev"
    JSON_SORT_KEYS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"  # 👈 Esta línea es clave
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Configuración para entorno de desarrollo.
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Configuración para entorno de producción.
    """
    DEBUG = False
