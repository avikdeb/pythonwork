from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, g
from managebill.applogic import login_manager, user_manager, email_manager

import os, sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        user = {'username': request.form['username']}
        return render_template('home.html', user = user)


@app.route('/login', methods=['POST'])
def login():

    form_username = request.form['username']
    form_password = request.form['password']

    # Calling the validator in login_manager script - username/password from the form is passed for validation
    # Sets the logged_in as true in session
    if login_manager.validate_login(form_username, form_password):
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route('/logout')
def logout():
    if session.get('logged_in'):
        session['logged_in'] = False
        return render_template('login.html')
    else:
        return render_template('home.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/newuser')
def newuser():
    return render_template('registration.html')


@app.route('/resetpass')
def resetpass():
    return render_template('resetpass.html')


@app.route('/doresetpass', methods=['POST'])
def do_resetpass():
    username = request.form['username']
    newpassword = request.form['newpassword']
    user_emailid = request.form['email']
    if user_manager.reset_password(username, newpassword):

        success_message = "Your password has been reset successfully. Please login to the application now."
        email_manager.send_email(user_emailid, success_message)
        return render_template('resetpass_result.html')
    else:
        return render_template('error.html')


@app.route('/dohome')
def dohome():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        session['logged_in'] = False
        return render_template('login.html')


@app.route('/createuser', methods=['POST'])
def createuser():
    user_dict = {
        "username" : request.form['username'],
        "password" : request.form['password'],
        "firstname" : request.form['firstname'],
        "lastname" : request.form['lastname'],
        "email" : request.form['email'],
        "mobile" : request.form['mobile']
    }

    if user_manager.create_user(user_dict):
        return render_template('signup_result.html', user = user_dict)
    else:
        return render_template('error.html')


@app.route('/addbill')
def addbill():
    return render_template('addbill.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)