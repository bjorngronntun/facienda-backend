from flask_restful import Resource, reqparse
import datetime
from models.note import NoteModel

class NoteList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'title',
        required=True,
        help='This field cannot be left blank'
    )
    parser.add_argument(
        'article_text',
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'date_created',
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'project_id',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )

    def get(self):
        return {'notes': [note.json() for note in NoteModel.query.all()]}

    def post(self):
        data = NoteList.parser.parse_args()
        y, m, d = data['date_created'].split('-')
        note = NoteModel(data['title'], data['article_text'], datetime.datetime(int(y), int(m), int(d)), data['project_id'])

        try:
            note.save_to_db()
        except:
            return {'message': 'An error occured inserting the note'}, 500

        return note.json(), 201
