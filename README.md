#Assignment 2

setup:
##Generating SQL Table
- Download Respository
- open mysql
- use mysql to run "todo_table.sql"
- use mysql to run "todo_table_fill.sql"
- you should have a database called "todo_list" with a table "list"


##Running the frontend
- Open the project in vscode
- Ensure that flask and mysqldb are installed according to the tutorial here https://www.geeksforgeeks.org/profile-application-using-python-flask-and-mysql/
- Ensure that the app config in app.py works with your MySQL server (not running on same port)
- In the terminal navigate to where you installed the CRUD-assignment
- Run py app.py

##Using the Site
- Open a browser
- navigate to http://localhost:5000/row
