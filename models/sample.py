from database import db


class Sample(db.Model):

    __tablename__ = 'sample'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    contens = db.Column(db.String(65536), nullable=False)

    def __repr__(self):
        return '<Sample {}>'.format(self.id)
