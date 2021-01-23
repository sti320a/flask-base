from exceptions import AuthException

from flask import Flask, redirect, render_template, request
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_basicauth import BasicAuth

from database import db, init_db
from models import Sample


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('config.Config')
    init_db(app)
    return app


app = create_app()
basic_auth = BasicAuth(app)


class ModelView(sqla.ModelView):

    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated. Refresh the page.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


admin = Admin(app, name='flask-base', template_mode='bootstrap3')
admin.add_view(ModelView(Sample, db.session))


@app.route('/')
def index():
    samples = Sample.query.all()
    return render_template('index.html', samples=samples)


@app.route('/create_sample', methods=['POST'])
def create_sample():
    contents = request.form['contents']
    sample = Sample(contents=contents)
    db.session.add(sample)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
