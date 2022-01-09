#import modules

from flask import *
import pymysql as pm

#connection with database

db=pm.connect(host="localhost",user="root",password="",database="taskmaster")

#create an cursor object.

cursor=db.cursor()
app=Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/allusers1")
def allusers1():
    selq="SELECT * FROM employee"
    cursor.execute(selq)
    result=cursor.fetchall()
    return render_template("allusers1.html",data=result)


@app.route("/adduser",methods=['POST'])
def adduser():
    ename=request.form['ename']
    contact=request.form['contact']
    email=request.form['email']
    password=request.form['password']
    salary=request.form['salary']
    insq="INSERT INTO employee(ename,contact,email,password,salary) VALUES ('{}','{}','{}','{}','{}')".format(ename,contact,email,password,salary)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for('allusers1'))
    except:
        db.rollback()
        return "Error in query"
    
@app.route("/delete")
def delete():
    eid=request.args['eid']
    delq="DELETE FROM employee WHERE eid={}".format(eid)
    try:
        cursor.execute(delq)
        db.commit()
        return redirect(url_for('allusers1'))
       
    except:
        db.rollback()
        return "Error in query"


@app.route("/edit")
def edit():
    eid=request.args['eid']
    sq="SELECT * FROM employee WHERE eid={}".format(eid)
    cursor.execute(sq)
    result=cursor.fetchone()
    return render_template('edit.html',data=result)


@app.route('/update',methods=['POST'])
def update():
    ename=request.form['ename']
   
    contact=request.form['contact']
    
    email=request.form['email']
    
    password=request.form['password']
    
    salary=request.form['salary']
    
    id=request.form['eid']
    upq="UPDATE employee SET ename='{}',contact='{}',email='{}',password='{}',salary='{}' WHERE eid={}".format(ename,contact,email,password,salary,id)
    try:
        cursor.execute(upq)
        db.commit()
        return redirect(url_for('allusers1'))
    except:
        db.rollback()
        return "Error in query"



if __name__=="__main__":
    app.run(debug=True)
    

