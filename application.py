from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = '123456789'
@app.route('/')
def index():
    return 'welcome to the login page yo'
@app.route('/profile/')
def profile(name):
    name = name
    access = {
        'Hitesh' : 'All Access'
    }
    tagline = {
        'Hitesh' : 'Mein Bata rha hun'
    }
    return render_template('profile.html',name=name,access = access[name],tagline = tagline[name])



# http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
@app.route('/accounts/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    data = {
        'test':'test',
        'gauransh':'gauru123'
    }
    name_data = {
        'test':'Hitesh' 
    }
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        
        
        # If account exists in accounts table in out database
        if data[username]== password:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['username'] = username
            # Redirect to home page
            return profile(name_data[username])
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username or Aapke liye Sir ne kuch nhi likha h :('
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)
@app.route('/accounts/logout')
def logout():
    return redirect(url_for('login'))
