import xlwt

def generate_excel(month, colslist):

    path = "download\\"
    book = xlwt.Workbook()
    sheet1 = book.add_sheet(month)

    col_heads = ["Billing Month", "From Date", "To Date", "Units Consumed", "Amount", "Due Date", "Last Date", "Amount Post Due Date", "Payment Status"]
    cols = colslist

    head_text = "%s"
    value_text = "%s"

    row = sheet1.row(0)

    for index, col in enumerate(col_heads):
        value = head_text % col
        row.write(index, value)

    row = sheet1.row(1)
    for index, col in enumerate(cols):
        value = value_text % col
        row.write(index, value)

    book.save(path+month+"_2018.xls")