from flask_migrate import Migrate
from config.database import db

def init_migrate(app):
    """
    Inicializa o Flask-Migrate com o aplicativo Flask.
    
    :param app: Instância do aplicativo Flask
    :return: Instância do Migrate
    """
    migrate = Migrate(app, db)
    return migrate
