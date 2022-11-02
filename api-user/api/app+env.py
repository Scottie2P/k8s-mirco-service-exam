from flask import Flask, render_template, jsonify
import psycopg2
import json
import os
app = Flask(__name__)

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
    # conn = psycopg2.connect(user="postgres",
    #                               password="Zxcv123!",
    #                               host="34.87.134.179",
    #                               port=5432,
    #                               database="bluepi")
    rowarray_list = create_dict()
    select_employee = "select * from public.user"
    cursor = conn.cursor()
    cursor.execute(select_employee)
    result = cursor.fetchall()

    for row in result:
        rowarray_list.add(row[0],({"first_name":row[1],"last_name":row[2],"dob":row[3]}))

    stud_json = json.dumps(rowarray_list, indent=4, sort_keys=True, default=str)
    return(stud_json)


@app.route("/api/v1/wallet")
def wallet():
    return 'api wallet OK !!'



@app.route("/")
def index():
    return render_template("index.html")


# Mock readiness check
@app.route("/ready")
def ready():
    return jsonify(
        backend='ready',
        db='ready',
        queue='ready'
    )
