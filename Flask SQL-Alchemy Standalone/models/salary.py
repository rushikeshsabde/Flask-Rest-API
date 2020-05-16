from database.db import db

class SalaryModel(db.Model):
    __tablename__ = 'salaries'
    emp_no = db.Column('emp_no', db.Integer, db.ForeignKey('employees.emp_no'), nullable=False)
    salary = db.Column('salary', db.Integer, nullable=True)
    from_date = db.Column('from_date', db.DateTime,primary_key=True)
    to_date = db.Column('to_date', db.DateTime, nullable=False)

    def __init__(self, emp_no, salary, from_date, to_date):
        self.emp_no = emp_no
        self.salary = salary
        self.from_date = from_date
        self.to_date = to_date

    def save_to_db(self):
        db.session.add(self)
        db.sessino.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(emp_no=id).all()

    def json(self, id):
        return{
            'emp_no':self.emp_no,
            'employee':[c.json() for c in self.employees.query.filter_by(emp_no=id).all()],
            'salary':self.salary,
            'from_date':self.from_date.strftime("%d/%m/%Y"),
            'to_date':self.to_date.strftime("%d/%m/%Y")
        }