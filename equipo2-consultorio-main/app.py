#punto de entrada que usa create_app() como punto de entrada
from src import create_app

app = create_app("src.config.DevelopmentConfig")

if __name__ == "__main__":
    app.run()
