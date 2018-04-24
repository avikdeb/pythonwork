from mypythonscripts.my_dboperations import *

# SQL
select_sql = "select * from usermaster"
insert_sql = "insert into usermaster(firstname, lastname, mobilenumber, email, collectorflag, notificationflag) " \
             "values(%s, %s, %s, %s, %d, %d)" \
             % ("'brar'", "'gurinder'", "'9899147405'", "'guri@mail.com'", 1, 1)
update_sql = "update usermaster set lastname = 'chawla' where idusermaster = '%d'" % (7)

sql_list = [select_sql, insert_sql, update_sql]

print_choice()
user_choice = input_choice()
db_operations(user_choice, sql_list)
