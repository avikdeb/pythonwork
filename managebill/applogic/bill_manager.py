import sqlite3
from managebill.applogic import login_manager

## To insert new bill
def create_bill(bill_dict):
    is_newbill = False
    from_date = bill_dict.get('fromdate')
    to_date = bill_dict.get('todate')
    units_consumed = bill_dict.get('unitsconsumed')
    amount = bill_dict.get('amount')
    amount_post_duedate = bill_dict.get('amountpostduedate')
    due_date = bill_dict.get('duedate')
    last_date = bill_dict.get('lastdate')
    payment_statusid = "1"

    create_bill_sql = "INSERT INTO melectricitybill (fromdate, todate, unitsconsumed, amount, amountpostduedate, duedate, lastdate, paymentstatusid) VALUES ('"+from_date+"', '"+to_date+"', '"+units_consumed+"', '"+amount+"', '"+amount_post_duedate+"', '"+due_date+"', '"+last_date+"', "+payment_statusid+");"
    print("[Create Bill SQL][bill_manager - create_bill]" + " " + create_bill_sql)

    conn = login_manager.connect_db()
    cursor = conn.execute(create_bill_sql)
    is_newbill = True
    conn.commit()
    cursor.close()
    conn.close()
    return is_newbill