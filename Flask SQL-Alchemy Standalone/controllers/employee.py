from flask_restful import Resource, reqparse, inputs
import datetime
from models.employee import EmployeeModel

class Employee(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('emp_no', type=int, required=True, help='Employee number is mandetory')
    parser.add_argument('birth_date', type=str, required=True, help="Date is mandetory")
    parser.add_argument('first_name', type=str, required=True, help="Firstname is mandetory")
    parser.add_argument('last_name', type=str, required=True, help="Lastname is mandetory")
    parser.add_argument('gender', type=str, required=True, help="Gender is mandetory")
    parser.add_argument('hire_date', type=str,required=True, help="Joining date is mandetory")

    def get(self, id):
        employee = EmployeeModel.find_by_id(id)
        if employee:
            return employee.json()
        else:
            return {'message':'Item not found'}, 404

    def post(self):
        data = Employee.parser.parse_args()
        format_str = '%d/%m/%Y' 
        id = data['emp_no']
        if EmployeeModel.find_by_id(id):
            return {'message':f'The item with {id} already exists'}, 400
        data['birth_date'] = datetime.datetime.strptime(data['birth_date'], format_str)
        data['hire_date'] = datetime.datetime.strptime(data['hire_date'], format_str)
        employee = EmployeeModel(emp_no=data['emp_no'], birth_date=data['birth_date'], first_name=data['first_name'], last_name=data['last_name'], gender=data['gender'], hire_date=data['hire_date'])
        try:
            employee.save_to_db()
            return employee.json(), 201
        except Exception as e:
            return {"message": f"An error occurred inserting the item and error is {e}."}, 500 
        

    def put(self,id):
        employee = EmployeeModel.find_by_id(id)
        if employee:
            data = Employee.parser.parse_args()
            format_str = '%d/%m/%Y' 
            data['birth_date'] = datetime.datetime.strptime(data['birth_date'], format_str)
            data['hire_date'] = datetime.datetime.strptime(data['hire_date'], format_str)
            try:
                employee.birth_date = data['birth_date']
                employee.first_name = data['first_name']
                employee.last_name = data['last_name']
                employee.gender = data['gender']
                employee.hire_date = data['hire_date']
                employee.save_to_db()
                return employee.json()
            except Exception as e:
                return {"message": f"An error occurred inserting the item and error is {e}."}, 500 
        else:
            {'message':'Item not found'},404


    def patch(self, id):
        employee = EmployeeModel.find_by_id(id)
        if employee:
            parser = reqparse.RequestParser()
            parser.add_argument('emp_no', type=int, required=False, help='Employee number is mandetory')
            parser.add_argument('birth_date', type=str, required=False, help="Date is mandetory")
            parser.add_argument('first_name', type=str, required=False, help="Firstname is mandetory")
            parser.add_argument('last_name', type=str, required=False, help="Lastname is mandetory")
            parser.add_argument('gender', type=str, required=False, help="Gender is mandetory")
            parser.add_argument('hire_date', type=str,required=False, help="Joining date is mandetory")

            data = parser.parse_args()
            format_str = '%d/%m/%Y' 
            if data['birth_date']:
                data['birth_date'] = datetime.datetime.strptime(data['birth_date'], format_str)
            if data['hire_date']:
                data['hire_date'] = datetime.datetime.strptime(data['hire_date'], format_str)

            print(data)
            for key,value in data.items():
                if data[key] and key!='emp_no':
                    setattr(employee, key, value)
            employee.save_to_db()
            return employee.json()
        else:
            {'message':'Item not found'},404

    def delete(self, id):
        employee = EmployeeModel.find_by_id(id)
        if employee:
            employee.delete_from_db()
            return {'message': f'Item with id {id} deletted successfully'}
        else:
            {'message':'Item not found'},404

