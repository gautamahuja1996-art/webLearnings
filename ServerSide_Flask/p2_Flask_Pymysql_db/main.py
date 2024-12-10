from flask import Flask, render_template, request

# importing pymysql which is an mysql db connector
import pymysql

app = Flask(__name__)

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
        print(n, e)

        # let's try to create a connection + cursor + query
        try:
            # creating a connection with the db
            connection = pymysql.connect(host='localhost', user='root', password='password1996', db='orm')

            # creating a curson to exchange data
            cursor = connection.cursor()

            # adding to the table
            # insert_query = f"INSERT INTO gym_users (name, email) VALUES ('{n}', '{e}');"
            insert_query = "INSERT INTO gym_users (name, email) VALUES (%s, %s);"

            # Provide the values for the placeholders as a tuple
            values = (n, e)
            cursor.execute(insert_query, values)
            connection.commit()
            data = cursor.fetchall()
            for row in data:
                print(row)
        except Exception as e:
            print(str(e))
        finally:

            # closing the curson and connection.
            cursor.close()
            connection.close()

    #  returning
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)