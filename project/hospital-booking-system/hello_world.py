from flask import Flask
from flask import request,session,abort
from flask import render_template
from flask_mysqldb import MySQL
import mysql.connector
#from AccountAPI import account_api



#mysql connection code
app = Flask(__name__)
#app.register_blueprint(account_api)


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

#redirect to user registration form
@app.route('/redirectuserregister')
def redirectuserregister():
    return render_template('userregistration.html')


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



#redirect to user registration form
@app.route('/redirecthospitalregister')
def redirecthuserregister():
    return render_template('hospitalregistration.html')



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
    cur.execute("INSERT INTO hospitalregister(name,number,email,services,address,city,state,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(name,number,email,services,address,city,state,password))
    mysql.connection.commit()
    cur.close()
    return render_template('main.html')






#search Hospital based on name and city
@app.route('/searchhospital' , methods=['POST' , 'GET'])
def searchhospital():
    name = request.form.get('name')
    city = request.form.get('city')
   # name = "malyala"
   # city = "hanamkonda"
    cur = mysql.connection.cursor()
    sql_query = """select * from hospitalregister where name = %s and city = %s"""
    cur.execute(sql_query, (name,city, ))
    row = cur.fetchone()
    
    n = 5 
    m = cur.rowcount
   # hlist = [[0]*n]*m
    hlist = []
   # count = 0
   # for row in record:
    if m == 0:
        return "THEIR ARE NO HOSPITAL PLEASE ENTER VALID RESULTS"
    hlist.append(row[0])
    hlist.append(row[1])
    hlist.append(row[2]) 
    hlist.append(row[3]) 
    hlist.append(row[4])
     
    cur.close()
    
    return render_template("hospitalview.html",hlist= hlist)

#after selecting hospital it will show all the doctors in that hospital
@app.route('/doctors' ,methods=['POST','GET'])
def doctors():
    hid = 21 
    cur = mysql.connection.cursor()
    sql_query = """select * from doctorstable where id=%s"""
    cur.execute(sql_query, (hid, ))
    record = cur.fetchall()

    cols = 3
    rows = cur.rowcount
    hlist = [[0 for i in range(cols)] for j in range(rows)] 
    count = 0
    for row in record:
        hlist[count][0] = row[2]
        hlist[count][1] = row[3]
        hlist[count][2] = row[4]
        count = count+1
    cur.close()

    return render_template("doctors.html",hlist=hlist)




#API FOR SHOWING TIME SLOTS OF THE SELECTED DOCTORS...
@app.route('/selecttimeslot' ,methods=['GET'])
def selecttimeslot():
    d = 21
    dd = 13

    cur = mysql.connection.cursor()
    sql_query = """select * from doctorstable where id = %s and doctorid = %s"""
    cur.execute(sql_query, (d,dd, ))
    record = cur.fetchone()
    mfrom = record[5]
    mto = record[6]
    afrom = record[7]
    ato = record[8]
    avgtime = record[9]

    #morning time slots
    mlist = []
    while mfrom < mto:
        mlist.append(mfrom)
        mfrom = mfrom + avgtime
    #afternoon time slots
    alist = []
    while afrom < ato:
        alist.append(afrom)
        afrom = afrom + avgtime

    return render_template('showtimeslots.html',mlist=mlist,alist=alist)



#API FOR ADDING THE TIME SLOTS TO THE USER TABLE AFTER SELECTING A TIMESLOT...
@app.route('/addtimeslottousertable' , methods=['POST'])
def addtimeslottousertable():
    hid =21
    doctorid =13
    userid =1
    time = request.form.get('time')

    cur = mysql.connection.cursor()
    sql_query = """update userregister set timeslot = %s, hospitalid = %s, doctorid = %s  where userid = %s"""
    cur.execute(sql_query,(time,hid,doctorid,userid,))
    mysql.connection.commit()
    cur.close()
    return  render_template("main.html")




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
     




















