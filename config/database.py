from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    """
    Configura a conexão com o banco de dados MySQL e inicializa o SQLAlchemy.
    
    :param app: Instância do aplicativo Flask
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://diego:1234@localhost/flask_crud_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
