from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    #return "Hey there! How are you doing?"
    return render_template('home.html')

@app.route('/about/')
def about():
    #return "Hey there! How are you doing?"
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)