from sqlalchemy import create_engine, text 
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string)

def load_emp_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from Emp"))
        emp=[]
        for row in result.all():
            emp.append(dict(row._mapping))
    return emp

def add_emp_to_db(data):
    with engine.connect() as conn:
        conn.execute(text("insert into Emp (name, email, phone) values (:name, :email, :phone)"), {'name':data['name'], 'email':data['email'], 'phone':data['phone']} )
        conn.commit()

def edit_emp_to_db(data):
    with engine.connect() as conn:
        conn.execute(text("insert into Emp (name, email, phone) values (:name, :email, :phone)"), {'name':data['name'], 'email':data['email'], 'phone':data['phone']} )
        conn.commit()