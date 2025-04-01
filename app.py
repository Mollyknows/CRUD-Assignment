from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import json
 
 
app = Flask(__name__)
app.secret_key = 'your secret key'
 
 #Configuration for accessing AWS RDS which is hosting my SQL database 
app.config['MYSQL_HOST'] = 'rds-mysql-tutorial.c1a4cwuciddj.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Bombom456!'
app.config['MYSQL_DB'] = 'TODO_List'

table = []
mysql = MySQL(app)

@app.route('/')
@app.route('/row', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def index():
    table = []
    #Kind of wish I had just used fetch for everything here but now it's too late to change it...
    if request.method == "POST" and 'taskEnter' in request.form and 'completeEnter' in request.form:
        task = request.form['taskEnter']
        deadline = request.form['completeEnter']
        if task and deadline != '':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO list VALUES (% s, % s, False, NULL)', (task, deadline))
            mysql.connection.commit()
    if request.method == 'PUT':
        data = request.get_json()
        location = data['location']
        oldText = data['old-string']
        newText = data['new-string']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE list SET deadline = %s WHERE deadline = %s AND id = %s', (newText, oldText, location))
        mysql.connection.commit()
    if request.method == 'DELETE':
        data = request.get_json()
        location = data['location']
        print(type(location))
        query = 'DELETE FROM list WHERE id = %d' % location
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        mysql.connection.commit()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM list')
    currentRow = cursor.fetchone()
    table.append(currentRow)
    for currentRow in cursor:
        table.append(currentRow)
    return render_template('row.html', table=table)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)