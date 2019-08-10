from flask import Flask
from flask import request,session,abort
from flask import render_template
from flask_mysqldb import MySQL
import mysql.connector
#import MySQLdb.cursors
#import re




#mysql connection code
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1998abc'
app.config['MYSQL_DB'] = 'myone'

mysql = MySQL(app)

#end mysql connection code



#MAIN API
@app.route('/hello')
def hello():
    return render_template('doctorview.html')


#ADD USER DETAILS TO THE DATABASE.............
@app.route('/print' , methods=['POST'])
def user_register():
    name = request.form.get('name') 
    email = request.form.get('email')
    city = request.form.get('city')
    state = request.form.get('state')
    password = request.form.get('password')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO userregister(name,email,city,state,password) VALUES(%s,%s,%s,%s,%s)",(name,email,city,state,password))
    mysql.connection.commit()
    cur.close()
    return render_template('main.html')






#ADD HOSPITAL TO THE DATABASE
@app.route('/addhospital' ,methods=['POST'])
def hospital_register():
    name = request.form.get('name')
    #session['my_hospital']=name
    number = request.form.get('number')
    email = request.form.get('email')
    services = request.form.get('services')
    address = request.form.get('address')
    city = request.form.get('city')
    state = request.form.get('state')
    password = request.form.get('password')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO doctorstable(name,number,email,services,address,city,state,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(name,number,email,services,address,city,state,password))
    mysql.connection.commit()
    cur.close()
    return render_template('loginpage.html')












#validate admin-hospital
@app.route('/validateuser' , methods=['POST','GET'])
def validate_user():
    email = request.form.get('email')
    password = request.form.get('password')
    cur = mysql.connection.cursor()
    # code for validating hospital login
    return "eeeee"








#VALIDATE USER
@app.route('/userlogin',methods=['GET'])
def userlogin():
    email = request.form.get('name')
    password = request.form.get('email')
    
    # code for validating user logins
    return "gg"
     




















