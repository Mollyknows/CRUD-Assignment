from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
 
 
app = Flask(__name__)
app.secret_key = 'your secret key'
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'todo_list'
 
 
mysql = MySQL(app)

@app.route('/')
@app.route('/row')
def index():
    table = []
    # print(str(request.form))
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM list')
    currentRow = cursor.fetchone()
    for currentRow in cursor:
        table.append(currentRow)
    print(str(table))
    return render_template('row.html', table=table) 

@app.route('/row', methods =['GET', 'POST'])
def newTask():
    msg = ""
    if request.method == "POST" and 'taskEnter' in request.form and 'completeEnter' in request.form:
        task = request.form['taskEnter']
        deadline = request.form['completeEnter']
        print(request.form['taskEnter'])
        print(request.form['completeEnter'])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO list VALUES ( % s, % s, + False)', (task, deadline))
        mysql.connection.commit()
        index()
    return render_template('row.html', msg=msg)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"))