from flask import Flask
from flask_restful import Api
from resources.project import ProjectList
from resources.milestone import MilestoneList
from resources.task import TaskList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(ProjectList, '/projects')
api.add_resource(MilestoneList, '/milestones')
api.add_resource(TaskList, '/tasks')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
