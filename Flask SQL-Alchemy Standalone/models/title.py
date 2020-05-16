from database.db import db

class TitleModel(db.Model):

    __tablename__ = 'titles'
    emp_no = db.Column('emp_no', db.Integer, db.ForeignKey('employees.emp_no'), nullable=False)
    title = db.Column('title', db.String(120), nullable=False)
    from_date = db.Column('from_date', db.DateTime, primary_key=True)
    to_date = db.Column('to_date', db.DateTime, nullable=False)

    def __init__(self, emp_no, title, from_date, to_date):
        self.emp_no = emp_no
        self.title = title
        self.from_date = from_date
        self.to_date = to_date

    def json(self):
        return{
            'emp_no':self.emp_no,
            'title':self.title,
            'from_date':self.from_date.strftime("%d/%m/%Y"),
            'to_date':self.to_date.strftime("%d/%m/%Y")
        }

    def save_to_db(self):
        db.session.add(self)
        db.sessino.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()