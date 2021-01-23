from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app: object) -> None:
    db.init_app(app)
    Migrate(app, db)
