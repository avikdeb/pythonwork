import sqlite3
from managebill.applogic import login_manager


## To reset user password
def reset_password(user, passwd):
    is_reset = False
    reset_sql = "UPDATE user SET password = '"+passwd+"'"+" WHERE username like '"+user+"';"
    print("[Password Reset SQL][user_manager - reset_password]" + " " + reset_sql)
    conn = login_manager.connect_db()
    cursor = conn.execute(reset_sql)
    conn.commit()
    is_reset = True
    return is_reset
