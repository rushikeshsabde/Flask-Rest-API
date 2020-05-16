from database.db import db

class DepartmentModel(db.Model):

    __tablename__ = 'departments'
    
    dept_no = db.Column('dept_no', db.String(20),primary_key=True)
    dept_name = db.Column('dept_name', db.String(120), nullable=True, unique=True)

    def __init__(self, dept_no, dept_name):
        self.dept_no = dept_no
        self.dept_name = dept_name

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(dept_no=id).first()   

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            'dept_no':self.dept_no,
            'dept_name':self.dept_name
        }