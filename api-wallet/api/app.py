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
class Wallet(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.String(100), nullable=False)


    def __int__(self, user_id, balance):
        self.user_id = user_id
        self.balance = balance

class create_dict(dict):  
    # __init__ function 
    def __init__(self):
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value


@app.route("/api/v1/wallet")
def user_get():
    conn = psycopg2.connect(user=os.environ['DB_USERNAME'],
                                  password=os.environ['DB_PASSWORD'],
                                  host=os.environ['DB_HOSTNAME_REPLICA'],
                                  port=os.environ['DB_PORT'],
                                  database=os.environ['DB_NAME'])

    rowarray_list = create_dict()
    select_user = "select * from public.wallet"
    cursor = conn.cursor()
    cursor.execute(select_user)
    result = cursor.fetchall()
    for row in result:
        rowarray_list.add(row[0],({"user_id":row[1],"balance":row[2]}))

    stud_json = json.dumps(rowarray_list, indent=4, sort_keys=True, default=str)
    return(stud_json)


# @app.route('/api/v1/wallet/create', methods=['POST'])
# def create():
#     conn = psycopg2.connect(user=os.environ['DB_USERNAME'],
#                                   password=os.environ['DB_PASSWORD'],
#                                   host=os.environ['DB_HOSTNAME_PRIMARY'],
#                                   port=os.environ['DB_PORT'],
#                                   database=os.environ['DB_NAME'])

#     user_id = request.form['user_id']
#     balance = request.form['balance']
#     # uuidOne = str(uuid.uuid1())
#     # print ("Printing my First UUID of version 1")
#     # print(uuidOne)
#     # insert_user = "INSERT INTO public.user(first_name, last_name, dob) VALUES ('{0}', '{1}', '{2}')".format(first_name,last_name,dob)
#     cursor = conn.cursor()
#     print(insert_user)
#     cursor.execute(insert_user)
#     conn.commit()
#     return 'insert seccess !'


# @app.route('/api/v1/wallet/delete/<id>/', methods=['DELETE'])
# def delete(id):
#     my_data = User.query.get(id)
#     db.session.delete(my_data)
#     db.session.commit()
#     return 'deleted !'


# @app.route('/api/v1/wallet/update/<id>', methods=['PUT'])
# def update(id):
#     my_date = Wallet.query.get(id)

#     if my_date.balance != None :
#         my_date.first_name = request.form['first_name']
#     elif  my_date.last_name != None :
#         my_date.last_name = request.form['last_name']
#     elif  my_date.dob != None :
#         my_date.dob = request.form['dob']
    
#     db.session.commit()
#     return 'update seccess !'


# health check
@app.route("/")
def index():
    return 'api OK !!'
