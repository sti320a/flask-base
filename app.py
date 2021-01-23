from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from database import db, init_db
from models import Sample


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('config.Config')
    admin = Admin(app, name='flask-base', template_mode='bootstrap3')
    admin.add_view(ModelView(Sample, db.session))
    init_db(app)
    return app


app = create_app()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
