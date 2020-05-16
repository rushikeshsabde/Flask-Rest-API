from models.department import DepartmentModel
from flask_restful import Resource, reqparse

class Department(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('dept_no', type=str, required=True, help='Department number is mandetory')
    parser.add_argument('dept_name', type=str, required=True, help='Department name is mandetory')

    def get(self, id):
        department = DepartmentModel.find_by_id(id)
        if department:
            return department.json()
        else:
            return {'message':'Department not found'}, 404

    def post(self):
        data = Department.parser.parse_args()
        id = data['dept_no']
        if DepartmentModel.find_by_id(id):
            return {'message':f'department with id {id} already exist'}
        department = DepartmentModel(dept_no=data['dept_no'], dept_name=data['dept_name'])
        try:
            department.save_to_db()
            return department.json(), 201
        except Exception as e:
            return {'message': f"An error occurred inserting the item and error is {e}."}, 500

    def put(self, id):
        department = DepartmentModel.find_by_id(id)
        if department:
            data = Department.parser.parse_args()
            department.dept_name = data['dept_name']
            department.save_to_db()
            return department.json()
        else:
            return {'message':'Department not found'}, 404
        
    def delete(self, id):
        department = DepartmentModel.find_by_id(id)
        if department:
            department.delete_from_db()
            return {'message', 'Department with id {id} is deleted'}
        else:
            return {'message':'Department not found'},404


        

            


