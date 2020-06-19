from db import db

class MilestoneModel(db.Model):
    __tablename__ = 'milestones'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    to_date = db.Column(db.String(80))

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship('ProjectModel')

    tasks = db.relationship('TaskModel', lazy='dynamic')

    def __init__(self, name, to_date, project_id):
        self.name = name
        self.to_date = to_date
        self.project_id = project_id

    def json(self):
        return {
            'name': self.name,
            'to_date': self.to_date,
            'tasks': [task.json() for task in self.tasks.all()],
            'project_id': self.project_id
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
