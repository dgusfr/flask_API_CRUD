from flask import Flask
from routes.item_routes import item_routes
from config.database import init_db
from config.migrate import init_migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

migrate = init_migrate(app)

app.register_blueprint(item_routes)

@app.route('/')
def home():
    return "API Flask funcionando! Acesse /items para listar os itens."

if __name__ == '__main__':
    app.run(debug=True)
