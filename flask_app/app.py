from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3690",
    database="form"
)

mycursor = mydb.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stud_name = request.form['studentName']
        father_name = request.form['fatherName']
        mother_name = request.form['motherName']
        phone_number = request.form['phoneNumber']
        email = request.form['email']
        dob = request.form['dob']
        address = request.form['address']
        b_grp = request.form['bloodGroup']
        dept = request.form['department']
        course = request.form['course']
        passwd = request.form['password']

        # Insert into MySQL
        sql = "INSERT INTO form_input (stud_name, father_name, mother_name, phone_number, email, dob, address, b_grp, dept, course, passwd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (stud_name, father_name, mother_name, phone_number, email, dob, address, b_grp, dept, course, passwd)
        mycursor.execute(sql, val)
        mydb.commit()

        return "Registration successful!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
