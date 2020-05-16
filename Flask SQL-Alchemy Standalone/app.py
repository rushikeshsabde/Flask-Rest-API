from flask import Flask
from flask_restful import Api
from controllers.employee import Employee
from controllers.department import Department
from controllers.salary import Salary

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Lumia630@localhost/employees"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "MySecretKey"

api.add_resource(Employee, "/employee", "/employee/<int:id>")
api.add_resource(Department, "/department", "/department/<string:id>")
api.add_resource(Salary, "/salary", "/salary/<string:id>")

if __name__ == "__main__":
    from database.db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
