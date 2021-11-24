import os
import json
import pyexcel

def main_runner(path):
    if type(path) == str:
        if path.endswith(".xlsx"):
            excel_reader_main.main(path=path)
        elif path.endswith(".xls"):
            print("this is a .xls\n    converting and processing....")
            new_path = (os.path.dirname(os.path.abspath(path))) + 'Book1_recreated.xlsx'
            pyexcel.save_book_as(file_name=path, dest_file_name=new_path)
            excel_reader_main.main(path=new_path)

class excel_reader_main():
    def main(path):
        return excel_reader_main.format_check(path) 

    def format_check(path):
        if path.endswith('xlsx'):
            try:
                my_dict = pyexcel.get_dict(file_name=path)
                from pyexcel._compact import OrderedDict
                isinstance(my_dict, OrderedDict)
                for key, values in my_dict.items():
                    print(key + " : " + ','.join([str(item) for item in values]))
            except: print('The file is empty.')
        else: return 'Unsupported format.\n  use ".xls" or "xlsm" or "xlsx"'

xlsx_path = r'C:\Users\renuk\OneDrive\Documents\Book.xlsx'
xls_path = r'C:\Users\renuk\OneDrive\Documents\Book1.xls'

main_runner(xlsx_path)