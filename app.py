from flask import Flask, jsonify, request
from flask_cors import CORS
import helper
app: Flask = Flask(__name__)
CORS(app)


# to register new student details (post)
@app.route('/add_student_details' , methods=['post'] )
def add_student_details():
    try:
        if request.method == 'POST':
            print(request)
            helper.create_student_database()
            helper.create_students_details_table()
            status = helper.register_student_details()
            return jsonify(status=status)
    except Exception as e:
        print(e)


# to get all student detials (get)
@app.route("/get_all_student_details", methods=['GET'])
def get_all_student_details():
    try:
        if request.method == 'GET':
            student_details = helper.get_all_student_details()
            return jsonify(student_details)

    except Exception as e:
        print(e)



#to update the student details(put)
"""
@app.route('/update_student_details', methods =['PUT'])
def update_student_details():
    try:
        if request.method == 'PUT':
            print(request)
            student_details_update_status = helper.student_details_upadte()

            return jsonify(status=student_details_update_status)

    except Exception as e:
        print(e)"""


# to delete the student details (delete)
@app.route('/delete_student_details' , methods =['DELETE'])
def delete_student_details():
    try:
        if request.method == 'DELETE':
            print(request)
            deletion_status = helper.delete_all_student_details()
            print(deletion_status)
            return jsonify(status=deletion_status)

    except Exception as e:
        print(e)


# to get the details of the student by roll number
@app.route('/get_student_details/<rollno>' , methods = ['GET'])
def get_student_details_by_roll(rollno):
    try:
        if request.method == 'GET':
            print(request)
            print(rollno)
            print("roll number of the student whose details should be retrived",rollno )
            retrived_details = helper.get_student_details_by_roll(rollno)
            return jsonify(status=retrived_details)

    except Exception as e:
        print(e)
# to update the details of the student by roll number
@app.route('/update_student_details/<rollno>' , methods = ['PUT'])
def update_student_details_by_roll(rollno):
    try:
        if request.method == 'PUT':
            print(request)
            print(rollno)
            print("roll number of the student whose details has to be updates",rollno )
            updation_status = helper.update_student_details_by_roll(rollno)
            return jsonify(status=updation_status)
    except Exception as e:
        print(e)


# to delete the details of the student by roll number
@app.route('/delete_student_details/<rollno>', methods=['DELETE'])
def delete_student_details_by_roll(rollno):
    try:
        if request.method == 'DELETE':
            print(request)
            print(rollno)
            print("roll number of the student whose details has to be deleted",rollno)
            deletion_status=helper.delete_student_details_by_roll(rollno)
            return jsonify(status=deletion_status)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
