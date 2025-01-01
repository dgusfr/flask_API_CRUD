from config.database import init_db

init_db(app)
migrate = init_migrate(app)