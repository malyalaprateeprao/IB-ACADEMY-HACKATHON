from flask import Flask
from flask import request,session,abort
from flask import render_template,Blueprint 
from flask_mysqldb import MySQL
import mysql.connector
from datetime import datetime,timedelta


#account_api = Blueprint('account_api', __name__)


#mysql connection code
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1998abc'
app.config['MYSQL_DB'] = 'myone'

mysql = MySQL(app)

#end mysql connection code
@app.route('/')
def me():
    #extract the name from db
    name = "kamineni"
    hid = 21
    cur = mysql.connection.cursor()
    sql_query = """select * from doctorstable where id = %s """
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
    
    return render_template("redirectadmin.html",name=name,hlist=hlist)

#ADD DOCTORS REDIRECT
@app.route('/redirectdoctorviews')
def redirectdoctorviews():
    return render_template("doctorregister.html")

#API WHICH TAKES DOCTOR DETAILS AND ADD TO THE DATABASE...
@app.route('/doctorregister' ,methods=['POST'])
def doctorregister():
    a = 21
    doctorid = request.form.get('doctorid')
    doctorname = request.form.get('doctorname')
    qualification = request.form.get('qualification')
    services = request.form.get('services')
    mfrom = request.form.get('mfrom')
    mto = request.form.get('mto')
    afrom = request.form.get('afrom')
    ato = request.form.get('ato')
    avgtime = request.form.get('avgtime')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO doctorstable(id,doctorid,doctorname,qualification,services,mfrom,mto,afrom,ato,avgtime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,doctorid,doctorname,qualification,services,mfrom,mto,afrom,ato,avgtime))
    mysql.connection.commit()
    cur.close()
    return "successfulli added"    


#api to view the patients of the doctor
@app.route('/doctorview',methods=['GET','POST'])
def doctorview():
    d = 21
    doctorid = request.form.get('doctorid')
    cur = mysql.connection.cursor()
    sql_query = """select * from userregister where hospitalid=%s and doctorid=%s"""
    cur.execute(sql_query, (d,doctorid, ))
    record = cur.fetchall()

    cols = 2
    rows = cur.rowcount
    hlist = [[0 for i in range(cols)] for j in range(rows)]
    count = 0
    for row in record:
        hlist[count][0] = row[1]
        hlist[count][1] = row[2]
        count = count+1
    cur.close()

    return render_template("doctorview.html",patients=rows,hlist=hlist)

    



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
    return "added"





