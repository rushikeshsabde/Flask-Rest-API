from database.db import db

class DeptEmpModel(db.Model):

    __tablename__ = 'dept_emp'
    emp_no = db.Column('emp_no', db.Integer, db.ForeignKey('employees.emp_no'),nullable=True)
    dept_no = db.Column('dept_no', db.String(20), db.ForeignKey('departments.dept_no'), nullable=True)
    from_date = db.Column('from_date', db.DateTime, primary_key=True)
    to_date = db.Column('to_date', db.DateTime, nullable=False)

    def __init__(cls, emp_no, dept_no, from_date, to_date):
        self.emp_no = emp_no
        self.dept_no = dept_no
        self.from_date = from_date
        self.to_date = to_date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            'emp_no':self.emp_no,
            'dept_no':self.dept_no,
            'from_date':self.from_date,
            'to_date':self.to_date
        }
