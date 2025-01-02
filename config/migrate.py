from flask_migrate import Migrate
from config.database import db

def init_migrate(app):
    return Migrate(app, db)
