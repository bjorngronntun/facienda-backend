from db import db

class ProjectModel(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    to_date = db.Column(db.String(80))

    def __init__(self, name, to_date):
        self.name = name
        self.to_date = to_date

    def json(self):
        return {
            'name': self.name,
            'to_date': self.to_date
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        deb.session.commit()
