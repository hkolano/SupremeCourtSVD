'''Reads from an ods file'''

from pyexcel_ods import get_data
import json

def read_ods():
    data = get_data("your_file.ods")
    print(json.dumps(data))

if __name__ == '__main__':
    read_ods()
