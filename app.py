from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from database import db
from models import Sample

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
admin = Admin(
    app,
    name='flask-base',
    template_mode='bootstrap3'
)
admin.add_view(ModelView(Sample, db.session))


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
