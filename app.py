from flask import Flask, render_template, request, session, redirect, url_for
import model

app = Flask(__name__)
app.secret_key = 'enterprise app'

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = model.signin(username,password)
        if not user == None:
            session['username']=user[2]
            session['role']=user[3]
        else:
            return render_template('signin.html',message='Wrong username or password.')
        if authorized('admin'):
            return render_template('admin.html')
        else:
            return render_template('user.html')
    else:
        return  render_template('signin.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        password = request.form['password']
        model.signup(firstname,lastname,username,password)
        return redirect(url_for('signin'))
    else:
        return  render_template('signup.html')

@app.route('/signout')
def signout():
    session.pop('username',None)
    session.pop('role',None)
    return redirect(url_for('home'))

@app.route('/user')
def user():
    if authenticated() and authorized('user'):
        return render_template('user.html')
    else:
        return redirect(url_for('signin'))

@app.route('/admin')
def admin():
    if authenticated() and authorized('admin'):
        return render_template('admin.html')
    else:
        return redirect(url_for('signin'))

def authorized(role):
    return 'role' in session and session['role'] == role

def authenticated():
    return 'username' in session

if __name__ == '__main__':
    app.run(debug=True)
