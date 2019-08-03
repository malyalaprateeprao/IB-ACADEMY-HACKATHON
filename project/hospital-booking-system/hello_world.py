from flask import Flask
from flask import request,session,abort
from flask import render_template
from flask_mysqldb import MySQL
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
    return render_template('main.html')


#ADD USER DETAILS TO THE DATABASE.............
@app.route('/print' , methods=['POST'])
def user_register():
    name = request.form.get('name') 
    number = request.form.get('number')
    email = request.form.get('email')
    city = request.form.get('city')
    state = request.form.get('state')
    password = request.form.get('password')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO rao12(name,number,email,city,state,password) VALUES(%s,%s,%s,%s,%s,%s)",(name,number,email,city,state,password))
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
    cur.execute("INSERT INTO rao13(name,number,email,services,address,city,state,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(name,number,email,services,address,city,state,password))
    mysql.connection.commit()
    cur.close()
    return render_template('loginpage.html')


#validate admin-hospital
@app.route('/validateuser' , methods=['POST','GET'])
def validate_user():
    name = request.form.get('name')
    password = request.form.get('password')
    cur = mysql.connection.cursor()
    my1 = "select name from rao13 where name = name"
    cur.execute(my1)
    myresult = cur.fetchall()
    #validate user
    idno = cur.execute("select id from rao13 where name = name")
    print(myresult)
    print(idno)
    return render_template('homepage.html',idno=idno)
    


#ADD DOCTORS BY HOSPITAL ADMIN
@app.route('/adddoctors' ,methods=['POST'])
def add_doctors():
    
    doctorid = request.form.get('doctorid')
    doctorname = request.form.get('doctorname')
    qualification = request.form.get('qualification')
    services = request.form.get('services')
    return render_template('homepage.html') 
