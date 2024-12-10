from flask import Flask, render_template, request

# To work better with flask server and SQLAlchemy ORM
from flask_sqlalchemy import SQLAlchemy

# importing pymysql
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# Adding configurations [related to the MYSQL database, username, password, server address, database name] to this flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password1996@localhost:3306/orm'

# Making an instance of SQLAlchemy. Connecting our ORM (making it aware about our flask server) with the flask app. This acts as a connector between our flask app and the ORM.
database = SQLAlchemy(app)

# Creating the Model class to handle the table in database.
# This class inherits from database.Model class which handle the SQL part
class Gym_users(database.Model):
    
    # making columns
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(20), nullable = False)
    email = database.Column(database.String(20), nullable = False, unique = True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    n = ''
    e = ''
    if request.method == 'POST':
        n = request.form.get('user_name')
        e = request.form.get('user_mail')
        
        # putting these entries in the db. Creating an instance of our Model class
        row = Gym_users(name = n, email=e)

        # adding to the database table
        database.session.add(row)

        # committing the change
        database.session.commit()

    #  returning
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)