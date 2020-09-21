import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host='mysql',
        user='root',
        passwd='mypassword'
        )

except Error as e:
    print("error while connecting to mysql" , e)


# create student database if not exist
def create_student_database():
    try:
        mycursor = mydb.cursor()
        mycursor.execute('show databases')
        mydatabases = mycursor.fetchall()

        database_create = True
        for database in mydatabases:
            print(database)
            student_db = "{0}".format(database[0])
            print(student_db, flush=True)

            if student_db == "student":
                print("student Database already created !", flush=True)
                database_create = False
                break
        if database_create:
            mycursor.execute("CREATE DATABASE student")
            print("student Database created !", flush=True)
    except Error as e:
        print("Error while creating student database", e)


# create student_details table if it does not exist
def create_students_details_table():
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd="mypassword"
        )

        mycursor = mydb.cursor()
        mycursor.execute("USE student")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()

        student_table_create = True
        for table in tables:
            student_table = "{0}".format(table[0])
            print( student_table , flush=True)

            if student_table == "student_details":
                print("student_details table already created !", flush=True)
                student_table_create = False
                break
        if student_table_create:
            mycursor.execute(
                "CREATE TABLE student_details ( student_name VARCHAR(50) ,  student_roll_number VARCHAR(50) NOT NULL PRIMARY KEY , dept VARCHAR(50) , year VARCHAR(50))")
            print("student_details table  created !", flush=True)

    except Error as e:
        print("Error while creating table ", e)


# register student details
def register_student_details(student_name,roll_no,dept,year):
    try:

        mydb = mysql.connector.connect(
            host='mysql',
            user='root',
            passwd='mypassword'
            )
        mycursor = mydb.cursor()
        mycursor.execute('USE student')
        sql = "INSERT into student_details values(%s,%s,%s,%s)"
        val = (student_name,roll_no,dept,year)
        mycursor.execute(sql,val)
        mydb.commit()
        return "student details register successfull"

    except Error as e :
        print("error while registering student details", e)


# method to get all student details
def get_all_student_details():
    try:
        mydb = mysql.connector.connect(
            host='mysql',
            user='root',
            passwd='mypassword'

        )
        mycursor=mydb.cursor()
        mycursor.execute('USE student')
        mycursor.execute('SELECT * from student_details')
        student_details = mycursor.fetchall()
        print(student_details)
        return student_details
    except Error as e :
        print("error while retriving all the student details" ,e)


# method to delete all student details
def delete_all_student_details(delete_rollnumber):
    try:
        mydb=mysql.connector.connect(
            host='mysql',
            user='root',
            passwd='mypassword'
            )
        mycursor=mydb.cursor()
        mycursor.execute("USE student")

        sql = "DELETE  from student_details where student_roll_number = '{delete_rollnumber}' ".format(delete_rollnumber = delete_rollnumber)
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        remaining_student_details = get_all_student_details()
        print("remaining_student_details" ,remaining_student_details)
        return "deletion of student details successful"
    except Error as e :
        print("error while deleting student details", e)


# method to get student details by roll number
def get_student_details_by_roll(rollno):
    try:
        mydb = mysql.connector.connect(
            host='mysql',
            user='root',
            passwd='mypassword'
        )
        mycursor = mydb.cursor()
        mycursor.execute("USE student")
        sql = " select * from student_details where student_roll_number = '{rollno}' ".format(rollno=rollno)
        print(sql)
        mycursor.execute(sql)
        student_details = mycursor.fetchone()
        print('details of the student ',student_details)
        return student_details
    except Error as e :
        print("error while retriving student details by roll number", e)


# method to update student details by roll number
def update_student_details_by_roll(rollno,update_column,update):
    try:
        mydb = mysql.connector.connect(
            host='mysql',
            user='root',
            passwd='mypassword'
        )
        mycursor = mydb.cursor()
        mycursor.execute("USE student")
        sql ="UPDATE student_details set {column_to_be_updated} ='{student_data_to_be_updated}' where student_roll_number = '{rollno}' ".format(column_to_be_updated=update_column,student_data_to_be_updated=update,rollno=rollno)
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        student_details = get_all_student_details()
        print("student_details", student_details)
        return "student details updation successfull"
    except Error as e :
        print("error while updating student details by roll number", e)


# method to delete student details by roll number
def delete_student_details_by_roll(rollno):
    try:
        mydb = mysql.connector.connect(
            host='mysql',
            user='root',
            passwd='mypassword'
        )
        mycursor = mydb.cursor()
        mycursor.execute("USE student")
        sql = "DELETE  from student_details where student_roll_number = '{rollno}' ".format(rollno = rollno)
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        remaining_student_details = get_all_student_details()
        print("remaining_student_details" ,remaining_student_details)
        return "deletion of student details successful"
    except Error as e :
        print("error while deleting student details", e)
