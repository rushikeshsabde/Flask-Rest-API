from database.db import db
import datetime
from models.salary import SalaryModel
from models.dept_emp import DeptEmpModel
from models.dept_manager import DeptManagerModel
from models.title import TitleModel

class EmployeeModel(db.Model):

    __tablename__ = "employees"
    emp_no = db.Column('emp_no',db.Integer, primary_key=True)
    birth_date = db.Column('birth_date', db.DateTime, nullable=False)
    first_name = db.Column('first_name',db.String(120), nullable=False)
    last_name = db.Column('last_name', db.String(120), nullable=False)
    gender = db.Column('gender', db.String(10), nullable=False)
    hire_date = db.Column('hire_date', db.DateTime, nullable=False)

    # backref
    salaries = db.relationship('SalaryModel', backref='employees', lazy = True)
    titles = db.relationship('DeptEmpModel', backref='employees', lazy = 'dynamic')
    dept_manager = db.relationship('DeptManagerModel', backref='employees', lazy = 'dynamic')
    dept_emp = db.relationship('TitleModel', backref='employees', lazy = 'dynamic')

    def __init__(self, emp_no, birth_date, first_name, last_name, gender, hire_date):
        self.emp_no = emp_no
        self.birth_date = birth_date
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.hire_date = hire_date

    def json(self):
        return {
            'emp_no':self.emp_no,
            'birth_date':self.birth_date.strftime("%d/%m/%Y"),
            'first_name':self.first_name,
            'last_name':self.last_name,
            'gender':self.gender,
            'hire_date':self.hire_date.strftime("%d/%m/%Y")
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(emp_no=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
