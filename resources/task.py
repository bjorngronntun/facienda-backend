from flask_restful import Resource, reqparse
import datetime
from models.task import TaskModel

class TaskList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        required=True,
        help='This field cannot be left blank'
    )
    parser.add_argument(
        'to_date',
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'milestone_id',
        type=int,
        required=True,
        help="Every task must have a milestone id"
    )

    def get(self):
        return {'tasks': [task.json() for task in TaskModel.query.all()]}

    def post(self):
        data = TaskList.parser.parse_args()
        y, m, d = data['to_date'].split('-')
        task = TaskModel(data['name'], datetime.datetime(int(y), int(m), int(d)), data['milestone_id'])
    
        try:
            task.save_to_db()
        except:
            return {'message': 'An error occured inserting the task'}, 500

        return task.json(), 201
