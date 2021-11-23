import os
import pyexcel
from pyexcel.ext import xlsx

class excel_reader_main():
    def main(path):
        return excel_reader_main.format_check(path) 

    def format_check(path):
        if path.endswith('xls') or path.endswith('xlsm') or path.endswith('xlsx'):
            name = 'Test2.csv'
            folder_path = file_name=os.path.dirname(path)
            pyexcel.save_as(folder_path, dest_file_name=folder_path+name)
            return 'saved as {0}'.format(name)
        else: return 'Unsupported format'

path = r'D:/Yashu/Projects/Python/excel_reader/Book.xlsx'

if type(path) == str:
    print(excel_reader_main.main(path=path))