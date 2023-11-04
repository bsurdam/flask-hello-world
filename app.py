import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('db_test')
def db_test():
    conn = psycopg2.connect("postgres://brandons_database_user:fLu3o48CwPeX33S01QMCtyCs6kgie8RG@dpg-cl37412uuipc738889dg-a/brandons_database")
    conn.close()
    return "Database Connection Successful"
