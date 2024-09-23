from flask import Flask, render_template,request
from database import add_emp_to_db, load_emp_from_db, get_emp_from_db, edit_emp_from_db, del_emp_from_db

app=Flask(__name__)


@app.route('/')
def Index():
    emp=load_emp_from_db()
    return render_template('index.html',empl=emp)

@app.route('/AddEmployee')
def AddEmp():
    return render_template('AddEmployee.html')

@app.route('/Added', methods=['post'])
def Added():
    data=request.form
    add_emp_to_db(data)
    return render_template('Added.html')

@app.route('/Update/<id>')
def Update(id):
    emp=get_emp_from_db(id)
    return render_template('Update.html',id=id, emp=emp)

@app.route('/Updated/<id>', methods=['post'])
def Updated(id):
    data=request.form
    edit_emp_from_db(id,data)
    return render_template('Updated.html')

@app.route('/Delete/<id>')
def Delete(id):
    del_emp_from_db(id)
    return render_template('Delete.html')

if __name__=="__main__":
    app.run(debug=True)

