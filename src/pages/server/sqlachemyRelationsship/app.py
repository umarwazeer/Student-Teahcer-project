from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_migrate import Migrate
from flask_wtf.file import FileField, FileAllowed, FileRequired


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/umarkhan/python projects/sqlachemyRelationsship/data.db'  # Replace with your MySQL connection details
engine = create_engine("sqlite:///data.db")
db = SQLAlchemy(app)
Session = sessionmaker(bind=engine)
migrate = Migrate(app, db)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.String(100))
    emp_id = db.Column(db.String(10), unique=True)
    emp_age = db.Column(db.Integer)
    emp_email = db.Column(db.String(100))
    # image_path = db.Column(db.String(200))

    def __init__(self, emp_name, emp_id, emp_age, emp_email, image_path):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_age = emp_age
        self.emp_email = emp_email
        self.image_path = image_path


@app.route('/api/employees', methods=['POST'])
def create_employee():
    emp_name = request.form.get('emp_name')
    emp_id = request.form.get('emp_id')
    emp_age = int(request.form.get('emp_age'))
    emp_email = request.form.get('emp_email')

    # Save the uploaded image to a file
    # image_file = request.files['imageData']
    image_path = f'path/to/save/images/{emp_id}.jpg'  # Modify this as per your file storage preferences
    # image_file.save(image_path)

    employee = Employee(emp_name=emp_name, emp_id=emp_id, emp_age=emp_age, emp_email=emp_email, image_path=image_path)
    db.session.add(employee)
    db.session.commit()
    return jsonify({'message': 'Employee created successfully'})

@app.route('/api/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    employee_list = []
    for employee in employees:
        employee_list.append({
            'id': employee.id,
            'emp_name': employee.emp_name,
            'emp_id': employee.emp_id,
            'emp_age': employee.emp_age,
            'emp_email': employee.emp_email,
            'image_url': f'http://localhost:2222/api/employees/{employee.emp_id}',  # Modify this as per your file storage preferences

        })
    return jsonify(employee_list)


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True, port=2222)
