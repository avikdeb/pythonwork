import xlrd

def open_file(path):
    book = xlrd.open_workbook(path)

    print(book.nsheets)

    print(book.sheet_names())

    first_sheet = book.sheet_by_index(0)

    print(first_sheet.row_values(0))

    cell = first_sheet.cell(0,0)

    print(cell)
    print(cell.value)

# __name__ returns the name of the module
# If __name__ is set to __main__ returns - The module run as main program
if __name__ == "__main__":
    path = "my_plan.xlsx"
    open_file(path)

print("\n Run again as usual - withut declaring main ... \n")
open_file("my_plan.xlsx")