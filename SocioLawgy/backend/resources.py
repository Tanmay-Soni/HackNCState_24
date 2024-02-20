from flask_restful import Resource, Api, marshal, fields, reqparse
from .models import db, Lawyer, Client, Case

api = Api(prefix='/api/v1')

class LawyerField(fields.Raw):
    def format(self, id):
        lawyer = db.session.query(Lawyer).filter_by(id=id).first()
        return {'id': lawyer.id, 'name': lawyer.name}
    
class ClientField(fields.Raw):
    def format(self, id):
        client = db.session.query(Client).filter_by(id=id).first()
        return {'id': client.id, 'name': client.name}

lawyer_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'speciality': fields.String,
    'experience': fields.Integer,
    'personal_website': fields.String,
    'cases': fields.List(fields.Nested({
        'id': fields.Integer,
        'name': fields.String,
        'case_type': fields.String,
        'description': fields.String,
        'summary': fields.String,
        'client': ClientField(attribute='client_id')
    }))
}

class Lawyers(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True)
        self.parser.add_argument('email', type=str, required=True)
        self.parser.add_argument('password', type=str, required=True)
        self.parser.add_argument('speciality', type=str, required=True)
        self.parser.add_argument('experience', type=int, required=True)
        self.parser.add_argument('personal_website', type=str, required=True)
    
    def get(self, email=None):
        if email is None:
            lawyers = db.session.query(Lawyer).all()
            return marshal(lawyers, lawyer_fields)
        else:
            lawyer = Lawyer.query.filter_by(email=email).first()
            if lawyer is None:
                return {'message': 'Lawyer not found'}, 404
            return marshal(lawyer, lawyer_fields)
        
    def post(self):
        args = self.parser.parse_args()
        lawyer = Lawyer(**args)
        db.session.add(lawyer)
        db.session.commit()
        return 'Lawyer added', 201
        
api.add_resource(Lawyers, '/lawyers', '/lawyers/<int:id>', '/lawyers/<string:email>')


client_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'cases': fields.List(fields.Nested({
        'id': fields.Integer,
        'name': fields.String,
        'case_type': fields.String,
        'description': fields.String,
        'summary': fields.String,
        'lawyer': LawyerField(attribute='lawyer_id')
    }))
}

class Clients(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True)
        self.parser.add_argument('email', type=str, required=True)
    
    def get(self, email):
        client = Client.query.filter_by(email=email).first()
        if client is None:
            return {'message': 'Client not found'}, 404
        return marshal(client, client_fields)
    
    def post(self):
        args = self.parser.parse_args()
        client = Client(**args)
        db.session.add(client)
        db.session.commit()
        return 'Client added', 201
        
api.add_resource(Clients, '/clients', '/clients/<int:id>', '/clients/<string:email>')

case_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'case_type': fields.String,
    'description': fields.String,
    'summary': fields.String,
    'client': ClientField(attribute='client_id'),
    'lawyer': LawyerField(attribute='lawyer_id')
}

class Cases(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True)
        self.parser.add_argument('case_type', type=str, required=True)
        self.parser.add_argument('description', type=str, required=True)
        self.parser.add_argument('summary', type=str, required=True)
        self.parser.add_argument('client_id', type=int, required=True)
        self.parser.add_argument('lawyer_id', type=int, required=True)
    
    def get(self, id):
        case = db.session.query(Case).get(id)
        if case is None:
            return {'message': 'Case not found'}, 404
        return marshal(case, case_fields)
    
    def post(self):
        args = self.parser.parse_args()
        case = Case(name=args['name'], case_type=args['case_type'], description=args['description'], summary=args['summary'], client_id=args['client_id'], lawyer_id=1)
        db.session.add(case)
        db.session.commit()
        return 'Case added', 201
    
    def put(self, id):
        args = self.parser.parse_args()
        case = db.session.query(Case).get(id)
        if case is None:
            return {'message': 'Case not found'}, 404
        case.name = args['name']
        case.case_type = args['case_type']
        case.description = args['description']
        case.summary = args['summary']
        case.client_id = args['client_id']
        case.lawyer_id = args['lawyer_id']
        db.session.commit()
        return 'Case updated', 200

    def delete(self, id):
        case = db.session.query(Case).get(id)
        if case is None:
            return {'message': 'Case not found'}, 404
        db.session.delete(case)
        db.session.commit()
        return 'Case deleted', 200

api.add_resource(Cases, '/cases','/cases/<int:id>')