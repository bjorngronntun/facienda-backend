from db import db

class NoteModel(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    article_text = db.Column(db.String(2000))
    date_created = db.Column(db.String(80))

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship('ProjectModel')

    # Use current timestamp for date_created?
    def __init__(self, title, article_text, date_created, project_id):
        self.title = title
        self.article_text = article_text
        self.date_created = date_created
        self.project_id = project_id

    def json(self):
        return {
            'title': self.title,
            'article_text': self.article_text,
            'date_created': self.date_created,
            'project_id': self.project_id
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
