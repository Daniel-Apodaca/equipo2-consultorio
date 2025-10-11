class Config:
    """
    Configuración base para la aplicación Flask.
    """
    SECRET_KEY = "dev"
    JSON_SORT_KEYS = False


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
