from flask_restful import Resource, reqparse
import datetime
from models.milestone import MilestoneModel

class MilestoneList(Resource):
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
        'project_id',
        type=int,
        required=True,
        help="Every milestone must have a project id"
    )

    def get(self):
        return {'milestones': [milestone.json() for milestone in MilestoneModel.query.all()]}

    def post(self):
        data = MilestoneList.parser.parse_args()
        y, m, d = data['to_date'].split('-')
        milestone = MilestoneModel(data['name'], datetime.datetime(int(y), int(m), int(d)), data['project_id'])

        try:
            milestone.save_to_db()
        except:
            return {'message': 'An error occured inserting the milestone'}, 500

        return milestone.json(), 201
