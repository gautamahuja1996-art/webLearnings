from flask import Flask, render_template, request, redirect, url_for, session

# to add security to our flask app
from werkzeug.utils import secure_filename

# importing math
import math

# importing flask_sqlalchemy to use ORM with flask
from flask_sqlalchemy import SQLAlchemy

# importing Mail class from flask mail module to send emails through our flask app.
from flask_mail import Mail

# to insert date
import datetime

# pymysql imports
import pymysql
pymysql.install_as_MySQLdb()

# importing user specific parameters from config.json
import json

# importing os module
import os

# opening the file
with open('config.json', 'r') as fp:
    all_data = json.load(fp)

# getting the data associated with params key
parameters = all_data['params']
creds = all_data['email_credentials']

app = Flask(__name__)

# setting the secret key
app.secret_key = 'gaut-1807'

# Adding upload folder location to the server, which means our server will save all the uploaded files to this location.
app.config['UPLOAD_FOLDER'] = parameters['upload_location']

# adding configuration to the app
if parameters['localserver']:
    app.config['SQLALCHEMY_DATABASE_URI'] = parameters['local_server_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = parameters['production_server_uri']

# Adding email configurations
app.config['MAIL_SERVER'] = creds['server']
app.config['MAIL_PORT'] = creds['port']

# Transport layer security: Ensures security between server and client
app.config['MAIL_USE_TLS'] = creds['use_tls']
app.config['MAIL_USERNAME'] = creds['username']
app.config['MAIL_PASSWORD'] = creds['password_for_gmail_smtp']

# creating an instance of ORM: SQLAlchemy and connecting it with our flask app
db = SQLAlchemy(app)

# creating an instance of Mail class. This will act as a connector between the flask app and email server.s
mail = Mail(app)

# creating a model class for contact me page
class ModelTable(db.Model):

    # writing table name
    __tablename__ = 'contact_me'

    # columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique = True)
    phone_number = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default = datetime.datetime.utcnow())

# creating a modeltable class for fetching/adding posts
class PostTable(db.Model):

    # tablename
    __tablename__ = 'blogpost'

    # columns
    id = db.Column(db.Integer, nullable= False, unique= True, primary_key= True, autoincrement= True)
    heading = db.Column(db.String(100), nullable= False)
    subheading = db.Column(db.String(100), nullable= False)
    author = db.Column(db.String(20), nullable= False)
    date = db.Column(db.DateTime, nullable= False)
    image = db.Column(db.String(40), nullable= False)
    content = db.Column(db.Text, nullable= False)
    slug = db.Column(db.String(50), nullable= False)

# defining routes for all html pages as at server's end you have to hit API's to render pages in the href attribute rather than writing the address of the html pages.
@app.route('/')
def index():

    # let's get all the posts
    all_posts = PostTable.query.all()

    # let's calculate the last page: round of to ceiling(total blogs/number of blogs in a page)
    last_page = math.ceil(len(all_posts) / parameters['posts_to_display'])

    # let's get the value of a key from the query string (current page number)
    page_number = request.args.get('page')
    # print(page_number, type(page_number))

    # if the client visits the home page with no 'page' argument in the query string, it returns none.
    if page_number == None:
        page_number = 1
    
    # typeconversion
    page_number = int(page_number)

    # calculating the blogs to send on the index page to display
    first_cut = (page_number-1)*parameters['posts_to_display']
    #  we can apply a condition on second cut, if it exceeds total number of posts
    second_cut = (page_number)*parameters ['posts_to_display']
    all_posts = all_posts[first_cut : second_cut]

    if page_number == 1:
        next_url = "/?page=" + str(page_number + 1)
        prev_url = "#"
    elif page_number == last_page:
        prev_url = "/?page=" + str(page_number - 1)
        next_url = "#"
    else:
        prev_url = "/?page=" + str(page_number - 1)
        next_url = "/?page=" + str(page_number + 1)

    # passing paramters to our template as well so that we can make changes in our html files.
    return render_template('index.html', params = parameters, blogs = all_posts, next_url = next_url, prev_url = prev_url)

@app.route('/about')
def about():
    return render_template('about.html', params= parameters)

@app.route('/contact')
def contact():
    return render_template('contact.html', params= parameters)

@app.route('/post')
def post():
    return render_template('post.html', params= parameters)

# route to handle contact me post request
@app.route('/contact_me', methods = ['GET', 'POST'])
def contact_me():

    # if request is post, getting the details from the form
    if request.method == 'POST':
        
        # getting form details
        user_name = request.form.get('user_name')
        user_mail = request.form.get('user_mail')
        user_phone = request.form.get('user_phone')
        user_message = request.form.get('user_message')
        
        # entering it in the db. Creating a row
        entry = ModelTable(name= user_name, email = user_mail, phone_number = user_phone, message = user_message)

        # let's add it
        db.session.add(entry)

        # let's commit it
        db.session.commit()

        # After entering data into db, let's send the email
        '''
        parameters-->
        subject: subject line of the email
        recipients: list of recipients
        '''
        mail.send_message(subject= 'Support Query Raised', 
                          sender= user_mail,
                          recipients= ['ahuja.gautam1996@gmail.com', 'gourichauhan2@gmail.com'], 
                          body= user_message + "\n" + user_phone)

    return render_template('index.html', params = parameters)

# creating a route with slug which will render a page our post page with our blog details
# will only accept get requests
@app.route('/blog/<post_slug>')
def blog(post_slug):

    # let's query the PostTable: Fetch the post whose slug (column) = post_slug
    # .all() --> Returns all the rows which satisfy the given query conditions
    # .first() --> Returns the first row which satisfies the given query conditions
    post_data = PostTable.query.filter_by(slug = post_slug).first()

    # let's return the post.html page with post_data so that we can changes in the template
    return render_template('blog.html', params = parameters, blog_data = post_data)

# creating a route for dashboard
@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():

    # let's check if a person coming to the dashboard route is logged in or not.
    # to check that, lets check if username key exists in session variable or not
    # if logged in, redirect them the admin page
    if "username" in session:
        return redirect(url_for('admin'))
    
    # if not logged in, either use can do get request or post request
    else:

        # if request is post, check credentials and if it's GET, render the dashboard.html
        if request.method == 'POST':
            
            # check credentials, if admin or not
            email = request.form.get('user_email')
            password = request.form.get('user_password')
            if email == parameters['admin_username'] and password == parameters['admin_password']:

                # creating a session variable for the user.
                session['username'] = email
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('dashboard'))
            
        # if request is get, and user is not logged in, let's give them dashboard page.
        else:
            return render_template('dashboard.html')
        

# admin page route
@app.route('/admin')
def admin():

    # user should be logged in
    if "username" in session:

        # fetching all the posts from db
        all_posts = PostTable.query.all()

        # sending it to the template
        return render_template('admin_page.html', params= parameters, blogs= all_posts)
    else:
        return redirect(url_for('dashboard'))
    
# for editing a post or adding a new post the url should be same as both process involves adding/updating information through a table, which means a single endpoint can handle it.
# post_id will hold the information to which post we are editing/ adding a new post
@app.route('/change/<post_id>', methods = ['GET', 'POST'])
def change(post_id):

    # user needs to be logged in for that
    if "username" in session:

        # if this endpoint receives post request, which means somebody has submitted the form to add/edit post
        if request.method == 'POST':

            # fetching all the form data
            heading = request.form.get('heading')
            subheading = request.form.get('subheading')
            author = request.form.get('author')
            slug = request.form.get('slug')
            image_path = request.form.get('image_path')
            content = request.form.get('content')
            
            # Once we have all the data, let's see if we have to add a blog or update the blog
            # that depends on the post_id
            if post_id == '0':

                # Adding a new blog
                entry = PostTable(heading=heading, subheading=subheading, author=author, date=datetime.datetime.utcnow(), image=image_path, content=content, slug=slug)

                # adding it to the db
                db.session.add(entry)
                db.session.commit()

                # After adding blog, redirect to the admin page
                return redirect(url_for('admin'))
            
            # if request is to update the blog, let's fetch it first
            else:

                # Get the first blog with id as post_id
                # When you query the db, you get the instance/object of the table (blog is the row/object/instance of the PostTable). So when you make changes to it and commit it, the changes are reflected in db. [ORM handles all the things.]
                blog = PostTable.query.filter_by(id = post_id).first()
                
                # updating the fields of blog
                blog.heading = heading
                blog.subheading = subheading
                blog.author = author
                blog.date = datetime.datetime.utcnow()
                blog.image = image_path
                blog.content = content
                blog.slug = slug

                # committing the changes to the session
                db.session.commit()

                # redirecting to admin panel
                return redirect(url_for('admin'))

        # if request is made to route, change/0, which means user wants to add post and if it's made to change/1 or any other id, it means user want to edit an existing post. In both cases we have to render change.html page to take data from the user for the blog
        # also let's render the template with post_id, so that submit knows where to hit the post request
        return render_template('change.html', params = parameters, post_id = post_id)
    
# route for logout
@app.route('/logout')
def logout():

    #  to logout user should be logged in
    if "username" in session:

        # removing username from session variable
        session.pop('username')

    # redirect to dashboard in both cases
    return redirect(url_for('dashboard'))

# route for file upload
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():

    # person should be logged in to upload the files on the server
    if "username" in session:

        # let's check the type of request
        if request.method == 'POST':

            # get the form data/ file
            # for that we use request.files method
            # the output would be a file object with file data/name everything.
            file = request.files['file_uploader']

            # we can use functions like save, filename to save the file or access the filename
            # saving the file in the given location

            # secure_filename sanitizes the filename that a person is uploading.
            file_save_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))

            # saving the file now
            file.save(file_save_path)

        # redirecting to the admin page
        return redirect(url_for('admin'))

# creating a post delete endpoint
@app.route('/delete/<post_id>')
def delete(post_id):

    # let's check if user is logged in
    if "username" in session:

        # let's get that post
        post = PostTable.query.filter_by(id = post_id).first()
        db.session.delete(post)
        db.session.commit()

    # returning to the admin page. If not logged in, it will be redirected to dashboard
    return redirect(url_for('admin'))
            

# Creating testing routes with slugs
'''
@app.route('/test')
def test1():
    return "<h1>Hello World</h1>"
@app.route('/test/<slug>')
def test(slug):
    return f"<h1>Hello {slug}</h1>"
'''
if __name__ == '__main__':
    app.run(debug=True)


