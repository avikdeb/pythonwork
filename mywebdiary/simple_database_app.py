import sqlite3
from flask import Flask
from flask import Flask, g, render_template
import os

app = Flask(__name__)


def connect_db():
    return sqlite3.connect("library.db")

## Before request callback - not connecting the database in view
## - it creates every time the action is evoked > Reusable global
@app.before_request
def before_request():
    g.db = connect_db()

@app.route('/')
def hello_world():
    ##db_connection = connect_db()
    ##cursor = db_connection.execute("SELECT id, name FROM author;")
    ##cursor = g.db.execute("SELECT id, name FROM author;")
    ## Now using a JOIN - to fetch data from 2 tables
    cursor = g.db.execute("""
        SELECT a.id, a.name, c.name 
        FROM author a INNER JOIN country c ON a.country_id = c.id;
    """)
    authors = [dict(id=row[0], name=row[1], country=row[2]) for row in cursor.fetchall()]

    ##return render_template('authors.html', authors = authors)
    ##return render_template('authors_template.html', authors=authors)
    return render_template('authors_template_conditional.html', authors=authors)


if __name__ == "__main__":

    app.run(debug=True)