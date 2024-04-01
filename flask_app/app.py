from flask import Flask, render_template, request
import mysql.connector

app=Flask(__name__)

Db=mysql.connector.connect(host="localhost", user="root", password="3690", database="form")
Cursor=Db.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        stud_name=request.form['studentName']
        father_name=request.form['fatherName']
        mother_name=request.form['motherName']
        phone_number=request.form['phoneNumber']
        email=request.form['email']
        dob=request.form['dob']
        address=request.form['address']
        b_grp=request.form['bloodGroup']
        dept=request.form['department']
        course=request.form['course']
        passwd=request.form['password']
        sql="insert into form_input (stud_name, father_name, mother_name, phone_number, email, dob, address, b_grp, dept, course, passwd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val=(stud_name, father_name, mother_name, phone_number, email, dob, address, b_grp, dept, course, passwd)
        Cursor.execute(sql, val)
        Db.commit()
        return "Registration Completed! Thank You."
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
