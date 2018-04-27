import sqlite3
from managebill.applogic import login_manager


## To reset user password
def reset_password(username, passwd):
    is_reset = False
    reset_sql = "UPDATE user SET password = '"+passwd+"'"+" WHERE username like '"+username+"';"
    print("[Password Reset SQL][user_manager - reset_password]" + " " + reset_sql)
    conn = login_manager.connect_db()
    cursor = conn.execute(reset_sql)
    conn.commit()
    conn.close()
    is_reset = True
    return is_reset

## To insert new user
def create_user(user_dict):
    is_created = False
    select_username = user_dict.get('username')
    select_password = user_dict.get('password')
    select_firstname = username = user_dict.get('firstname')
    select_lastname = username = user_dict.get('lastname')
    select_email = user_dict.get('email')
    select_mobile = user_dict.get('mobile')
    select_adminflag = "0"

    create_user_sql = "INSERT INTO user (username, password, firstname, lastname, email, mobile, adminflag) VALUES ('"+select_username+"', '"+select_password+"', '"+select_firstname+"', '"+select_lastname+"', '"+select_email+"', '"+select_mobile+"', "+select_adminflag+");"
    print("[User Create SQL][user_manager - create_user]" + " " + create_user_sql)

    conn = login_manager.connect_db()
    cursor = conn.execute(create_user_sql)
    is_created = True
    conn.commit()
    cursor.close()
    conn.close()
    return is_created