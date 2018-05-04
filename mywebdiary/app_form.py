from flask import Flask, flash, render_template, request


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('basic_form.html')
    elif request.method == 'POST':
        kwargs = {
            'title': request.form['title'],
            'isbn': request.form['isbn'],
            'author': request.form['author'],
            'secret_key': request.form['SECRET_KEY'],
            'submit_value': request.form['submit'],
        }
        return render_template('basic_form_result.html', **kwargs)

if __name__ == "__main__":
    app.run(debug=True)