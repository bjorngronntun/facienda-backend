from flask_restful import Resource, reqparse
import datetime
from models.project import ProjectModel

class ProjectList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'to_date',
        required=True,
        help="This field cannot be left blank"
    )

    # Get all projects
    def get(self):
        return {'projects': [project.json() for project in ProjectModel.query.all()]}

    # Post a new project
    def post(self):
        data = ProjectList.parser.parse_args()
        y, m, d = data['to_date'].split('-')
        project = ProjectModel(data['name'], datetime.datetime(int(y), int(m), int(d)))

        try:
            project.save_to_db()
        except:
            print('Inserting {} {}'.format( data['name'], data['to_date']))
            return {'message': 'An error occured inserting the project'}, 500

        return project.json()
