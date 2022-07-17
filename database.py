import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def conn():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASS"),
        database=os.getenv("DB")
    )
    return conn

def select(query, values, conn):
    mycursor = conn.cursor()
    mycursor.execute(query, values)
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    json_data = []
    for result in myresult:
        json_data.append(dict(zip(row_headers, result)))
    return json_data

def insert(query, val, conn):
    mycursor = conn.cursor()
    mycursor.execute(query, val)
    conn.commit()