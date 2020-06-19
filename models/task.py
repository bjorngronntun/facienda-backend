from db import db

class TaskModel(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    to_date = db.Column(db.String(80))
    done = db.Column(db.Boolean())

    milestone_id = db.Column(db.Integer, db.ForeignKey('milestones.id'))
    milestone = db.relationship('MilestoneModel')

    def __init__(self, name, to_date, milestone_id):
        self.name = name
        self.to_date = to_date
        self.done = False
        self.milestone_id = milestone_id

    def json(self):
        return {
            'name': self.name,
            'to_date': self.to_date,
            'done': self.done,
            'milestone_id': self.milestone_id
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
