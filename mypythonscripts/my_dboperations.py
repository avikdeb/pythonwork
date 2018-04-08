import mysql.connector

# User choice and input functions
def print_choice():
    print("Select Operation:")
    print("[S] SELECT")
    print("[I] INSERT")
    print("[U] UPDATE")

def input_choice():
    choice = input("Enter operation code: \n")
    return choice

def db_operations(choice, sql_list):
    if choice == "S":
        select_ops(sql_list[0])
    elif choice == "I":
        insert_ops(sql_list[1])
    elif choice == "U":
        update_ops(sql_list[2])
    else:
        print("[ERROR] Invalid selection.")
#--------------------------------------------------------------------------------------------------

# Database operation functions
# Connect to DB with the credentials and returns Connection object
def create_connection():
    dbuser = 'root'
    dbpasswd = 'root'
    dbhost = 'localhost'
    dbschema = 'managebilldb'
    conn = mysql.connector.connect(user=dbuser, password=dbpasswd, host=dbhost, database=dbschema)
    return conn

# Close databse connection
def close_connection(conn):
    conn.close()
    print("[INFO] Database connection closed")

# Executes SELECT operation
def select_ops(select_sql):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(select_sql)
    try:
        results = cursor.fetchall()
        for row in results:
            for index in range(0, len(row) - 1):
                print('column ', index, ' -- ', row[index])
    except:
        print("[ERROR] Unable to fetch data")
    finally:
        close_connection(conn)

# Executes INSERT operation
def insert_ops(insert_sql):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(insert_sql)
        conn.commit()
        print("[SUCCESS] Records INSERT successful")
    except:
        conn.rollback()
        print("[ERROR] Records INSERT fail - ROLLBACK successfully")
    finally:
        close_connection(conn)

# Executes UPDATE operation
def update_ops(update_sql):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(update_sql)
        conn.commit()
        print("[SUCCESS] UPDATE Records successful")
    except:
        conn.rollback()
        print("[ERROR] Records UPDATE fail - ROLLBACK successfully")
    finally:
        close_connection(conn)