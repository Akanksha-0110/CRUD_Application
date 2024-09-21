from flask import Flask, render_template,request
from database import add_emp_to_db, load_emp_from_db

app=Flask(__name__)


@app.route('/')
def Index():
    emp=load_emp_from_db()
    return render_template('index.html',emp=emp)

@app.route('/AddEmployee')
def AddEmp():
    return render_template('AddEmployee.html')

@app.route('/Update')
def Update():
    return render_template('Update.html')

@app.route('/Success', methods=['post'])
def EmpDetails():
    data=request.form
    add_emp_to_db(data)
    return render_template('Success.html')

if __name__=="__main__":
    app.run(debug=True)

