from flask import Flask, render_template, jsonify , request 
import psycopg2
import json
import os
import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{}:{}@{}/{}".format(os.environ['DB_USERNAME'], os.environ['DB_PASSWORD'], os.environ['DB_HOSTNAME_PRIMARY'], os.environ['DB_NAME'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(100), nullable=False)

    def __int__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

class create_dict(dict):  
    # __init__ function 
    def __init__(self):
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value


@app.route("/api/v1/user")
def user_get():
    conn = psycopg2.connect(user=os.environ['DB_USERNAME'],
                                  password=os.environ['DB_PASSWORD'],
                                  host=os.environ['DB_HOSTNAME_REPLICA'],
                                  port=os.environ['DB_PORT'],
                                  database=os.environ['DB_NAME'])

    rowarray_list = create_dict()
    select_user = "select * from public.user"
    cursor = conn.cursor()
    cursor.execute(select_user)
    result = cursor.fetchall()
    for row in result:
        rowarray_list.add(row[0],({"first_name":row[1],"last_name":row[2],"dob":row[3]}))

    stud_json = json.dumps(rowarray_list, indent=4, sort_keys=True, default=str)
    return(stud_json)


@app.route('/api/v1/user/create', methods=['POST'])
def create():
    conn = psycopg2.connect(user=os.environ['DB_USERNAME'],
                                  password=os.environ['DB_PASSWORD'],
                                  host=os.environ['DB_HOSTNAME_PRIMARY'],
                                  port=os.environ['DB_PORT'],
                                  database=os.environ['DB_NAME'])

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    # uuidOne = str(uuid.uuid1())
    # print ("Printing my First UUID of version 1")
    # print(uuidOne)
    insert_user = "INSERT INTO public.user(first_name, last_name, dob) VALUES ('{0}', '{1}', '{2}')".format(first_name,last_name,dob)
    cursor = conn.cursor()
    print(insert_user)
    cursor.execute(insert_user)
    conn.commit()
    return 'insert seccess !'


@app.route('/api/v1/user/delete/<id>/', methods=['DELETE'])
def delete(id):
    my_data = User.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    return 'deleted !'


@app.route('/api/v1/user/update/<id>', methods=['PUT'])
def update(id):
    my_date = User.query.get(id)

    if my_date.first_name != None :
        my_date.first_name = request.form['first_name']
    elif  my_date.last_name != None :
        my_date.last_name = request.form['last_name']
    elif  my_date.dob != None :
        my_date.dob = request.form['dob']
    
    db.session.commit()
    return 'update seccess !'


# health check
@app.route("/")
def index():
    return 'api OK !!'
