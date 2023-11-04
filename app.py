import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://brandons_database_user:fLu3o48CwPeX33S01QMCtyCs6kgie8RG@dpg-cl37412uuipc738889dg-a/brandons_database")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgres://brandons_database_user:fLu3o48CwPeX33S01QMCtyCs6kgie8RG@dpg-cl37412uuipc738889dg-a/brandons_database")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Creation Successful"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgres://brandons_database_user:fLu3o48CwPeX33S01QMCtyCs6kgie8RG@dpg-cl37412uuipc738889dg-a/brandons_database")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"
