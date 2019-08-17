from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Role(db.Model):
    __tablename__ = 'role'
    __bind_key__ = 'manual_admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    type = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Role %r>' % self.name
