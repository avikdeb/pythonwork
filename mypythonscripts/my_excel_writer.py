import xlwt


# ----------------------------------------------------------------------
def main():
    """"""

    month = "may"
    book = xlwt.Workbook()
    sheet1 = book.add_sheet(month)

    col_heads = ["Billing Month", "From Date", "To Date", "Units Consumed", "Amount", "Due Date", "Last Date",
                     "Amount Post Due Date", "Payment Status"]
    cols = ["January", "15/5/2018", "31/5/2018", "400", "3200", "7/6/2018", "15/6/2018", "3400", "Payment Due"]

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

    book.save(month+"_2018.xls")


# ----------------------------------------------------------------------
if __name__ == "__main__":
    main()