#!/usr/bin/env python3

"""Import SQL Functions And Run Them"""

MySQLAdd = __import__('MySQL').MySQL
MySQLRemove = __import__('MySQL').remove_all_records_from_table

if __name__ == '__main__':
    MySQLAdd()
    MySQLRemove()
