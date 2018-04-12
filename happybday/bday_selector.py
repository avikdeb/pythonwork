import xlrd
import xlwt
import datetime

# Returns email id if today matches the birth date in excel
def get_emailid_by_date(filepath, today):

    select_email = ""
    today_dd_mm = today.strftime('%d-%b')
    print ("Today's date is", today_dd_mm)

    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_index(0)

    for row_idx in range(1, worksheet.nrows):
        bday_dd = worksheet.cell(row_idx, 1).value
        #bday_mm = worksheet.cell(row_idx, 2).value
        #bday_dd_mm = str(bday_dd).replace(".0","")+"-"+str(bday_mm)
        email_id = worksheet.cell(row_idx, 2).value

        if today_dd_mm == bday_dd:
            select_email = email_id

    return select_email






