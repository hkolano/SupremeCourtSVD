import pandas as pd
from pyexcel_ods import get_data
import pyexcel as pe
import json

# data = get_data("consolidated_data.ods")

sheet = pe.get_book(file_name="consolidated_data.ods")
print(sheet)
# for i in range(len(data)-1):
#     print(json.dumps(data[i]))
