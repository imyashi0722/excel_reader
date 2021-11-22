# import os, os.system("pip install xlrd")
# import xlrd

class excel_reader_main():
    def main(path):
        return "responding"

path = "D:\\Yashu\\Projects\\Python\\excel_reader\\Book.xlsx"

#if path.endswith("xlsx"):
#    import openpyxl as xl
#    wb = xl.load_workbook("yourfile.xlsx")
#    wb.save("file.xls")

if type(path) == str:
    print(excel_reader_main.main(path=path))