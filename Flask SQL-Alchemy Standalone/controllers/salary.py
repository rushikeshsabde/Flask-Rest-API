from flask_restful import Resource, reqparse
from models.salary import SalaryModel
import datetime

class Salary(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('emp_no', type=int, required=True, help='Employee number is mandetory')
    parser.add_argument('salary', type=int, required=True, help='salary is mandetory')
    parser.add_argument('from_date',type=str, required=True, help='Form date is mandetory')
    parser.add_argument('to_date', type=str, required=True, help='To date is mandetory')

    def get(self, id):
        salary = SalaryModel.find_by_id(id)
        if salary:
            return {'salary': list(map(lambda x: x.json(id), SalaryModel.query.filter_by(emp_no=id)))}

    def post(self):
        data = parser.parse_args()
        format_str = '%d/%m/%Y' 
        data['from_date'] = datetime.datetime.strptime(data['from_date'], format_str)
        data['to_date'] = datetime.datetime.strptime(data['to_date'], format_str)
        salary = SalaryModel(data['emp_no'], data['salary'], data['from_date'], data['to_date'])
        try:
            salary.save_to_db()
            return salary.json(), 201
        except Exception as e:
            return {'message':e}, 500