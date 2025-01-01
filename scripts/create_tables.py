from app import app
from config.database import db
from models.item import Item

with app.app_context():
    db.create_all()
