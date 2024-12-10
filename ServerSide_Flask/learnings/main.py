'''
When you close the browser, the session is deleted by the server for that client/browser, but in real life scenarios even after you close the borwser, you can login to the server after again opening it or if you check mark 'remember me', it helps to remember your credentials. This can be achieved by making the session available for a bit longer, by using 'permanent_session_lifetime'
'''


# importing flask
from flask import Flask, render_template, redirect, url_for, request, session

# for specifying the duration to store a session
from datetime import timedelta

# creating an app
app = Flask(__name__)

# creating a secret key
app.secret_key = "9650-gautam-1996"

# keeping the session intact for 2 mins, not matter how many time you close the browser.
app.permanent_session_lifetime = timedelta(minutes=2)

admin_name = 'Gautam chourasia'

# creating routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<extended_information>')
def user(extended_information):

    user_name = 'Gautam'
    return render_template('user.html', username = extended_information)

@app.route('/loop')
def loop():
    defaulters = ['Gautam', 'Rishabh', 'Chirag']
    return render_template('defaulters.html', defaulters = defaulters)

@app.route('/admin')
def admin():
    if admin_name == 'Gautam':
        return redirect(url_for('user', extended_information = 'Gautam Ahuja'))
    else:
        return redirect(url_for('index'))
    
@app.route('/login', methods = ['GET', 'POST'])
def login():

    # if user submits the form, hits the post requst, check/authenticate them
    if request.method == 'POST':
        name = request.form.get('name')
        session['username'] = name
        
        # making the session false
        session.permanent = True
        return redirect(url_for('name_display'))
    
    # if they hit a get request: 2 possibilities: they are not logged in and requesting the login page or they are logged in an reqeusting the login page
    else:

        # if user is logged in, which means 'username' key will be there in the session
        if 'username' in session:
            return redirect(url_for('name_display'))
        else:
            return render_template('login.html')

@app.route('/name_display')
def name_display():

    # checking if there is a username key in the session, which means user has logged in
    if "username" in session:

        # getting user name from the session
        user_name = session['username']
        return f"Hello {user_name}"
    
    # if someone is not logged in but is trying to access /name_display route
    # redirect them to the login page
    else:
        return redirect(url_for('login'))

# creating a route for logout
@app.route('/logout')
def logout():

    # removing the data associated with username key from the session using pop function
    session.pop('username', None)

    # redirecting back to the login page
    return redirect('login')


# running the app
if __name__ == '__main__':
    app.run(debug=True)