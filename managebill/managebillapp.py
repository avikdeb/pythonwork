from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, g, send_file, make_response
from managebill.applogic import login_manager, user_manager, email_manager, bill_manager, excel_maker

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

@app.route('/gohome', methods=['POST'])
def gohome():
    if session.get('logged_in'):
        username = request.form['username']
        user = { "username": username}
        return render_template('home.html', user=user)
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


@app.route('/addbill', methods=['GET','POST'])
def addbill():
    puser={ "username": request.form['username']}
    print(request.form['username'])
    print(puser)
    return render_template('addbill.html', puser=puser)


@app.route('/createbill', methods=['POST'])
def createbill():
    print("username --> " + request.form['username'])
    bill_dict = {
        "username": request.form['username'],
        "billingmonth": request.form['billingmonth'],
        "fromdate": request.form['fromdate'],
        "todate": request.form['todate'],
        "unitsconsumed": request.form['unitsconsumed'],
        "amount": request.form['amount'],
        "amountpostduedate": request.form['amountpostduedate'],
        "duedate": request.form['duedate'],
        "lastdate": request.form['lastdate']
    }
    print("username --> "+request.form['username'])
    if bill_manager.create_bill(bill_dict):
        return render_template('newbill_result.html', newbill=bill_dict)
    else:
        return render_template('error.html')

@app.route('/create_excel', methods=['POST'])
def create_excel():

    col_list = [
        request.form['billingmonth'],
        request.form['fromdate'],
        request.form['todate'],
        request.form['unitsconsumed'],
        request.form['amount'],
        request.form['amountpostduedate'],
        request.form['duedate'],
        request.form['lastdate'],
        request.form['paymentstatus']
    ]

    bill_dict = {
        "username": request.form['username'],
        "billingmonth": request.form['billingmonth'],
        "fromdate": request.form['fromdate'],
        "todate": request.form['todate'],
        "unitsconsumed": request.form['unitsconsumed'],
        "amount": request.form['amount'],
        "amountpostduedate": request.form['amountpostduedate'],
        "duedate": request.form['duedate'],
        "lastdate": request.form['lastdate']
    }

    excel_maker.generate_excel(request.form['billingmonth'], col_list)
    return render_template('save_excel_result.html', newbill=bill_dict)


@app.route('/download', methods=['POST'])
def download():
    excel_filename = request.form['filename']
    try:
        return send_file('C:/pythonwork/managebill/static/download/'+excel_filename+'_2018.xls', attachment_filename=excel_filename+'_2018.xls')
    except Exception as e:
        return str(e)

@app.route("/consumption_plot.png", methods=['GET', 'POST'])
def consumption_plot():
    import datetime
    from io import BytesIO
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)