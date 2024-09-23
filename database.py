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

def get_emp_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from Emp where id=:val"),{'val':id})
        emp=[]
        for row in result.all():
            emp.append(dict(row._mapping))
    return emp

def edit_emp_from_db(id,data):
    with engine.connect() as conn:
        conn.execute(text("update Emp set name=:name, email=:email, phone=:phone where id=:val"),{'name':data['name'], 'email':data['email'], 'phone':data['phone'], 'val':id})
        conn.commit()

def del_emp_from_db(id):
    with engine.connect() as conn:
        conn.execute(text("Delete from Emp where id=:val"),{'val':id})
        conn.commit()
