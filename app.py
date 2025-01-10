from flask import Flask
from config.database import init_db
from config.migrate import init_migrate
from routes.product_routes import product_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask_user:1234@localhost/flask_crud_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)
migrate = init_migrate(app)

app.register_blueprint(product_routes)

if __name__ == '__main__':
    app.run(debug=True)
