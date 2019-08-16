from flask import Flask
from flask import request,session,abort
from flask import render_template
from flask_mysqldb import MySQL
import mysql.connector
#import MySQLdb.cursors
#import re
from datetime import datetime,timedelta

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
    return render_template("doctorview.html")



#API WHICH TAKES DOCTOR DETAILS AND ADD TO THE DATABASE...
@app.route('/doctorviews' ,methods=['POST'])
def doctorviews():
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





