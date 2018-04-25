import sqlite3

# Below are codes to validate login against database
def connect_db():
    return sqlite3.connect("managebill.db")

## To check valid user
def validate_login(user, passwd):
    is_valid = False
    login_sql = "SELECT username, password FROM user WHERE username LIKE '"+user+"'"+" AND password like '"+passwd+"';"
    print("[Login SQL][login_manager - validate_login]" + " " + login_sql)
    cursor = connect_db().execute(login_sql)
    for row in cursor.fetchall():
        if row[0] == user and row[1] == passwd:
            is_valid = True
    return is_valid

## To get the user dict based on username
def get_user_by_username(user, passwd):

    user_sql = "SELECT * FROM user WHERE username LIKE '"+user+"'"+" AND password like '"+passwd+"';"
    print("[Login SQL][login_manager - get_user_by_username]" + " " + user_sql)
    cursor = connect_db().execute(user_sql)
    user = [dict(userid=row[0], username=row[1], password=row[2], firstname=row[3], lastname=row[4],  ) for row in cursor.fetchall()]
    print(user)
    return user