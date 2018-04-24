from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    user = { 'username' : 'Avik'}
    return render_template('home.html', title = 'Home', user = user)

@app.route('/about/')
def about():
    user = {'username': 'Guri'}
    return render_template('about.html', title = 'About', user = user)

@app.route('/help/')
def help():
    #return "Hey there! How are you doing?"
    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)