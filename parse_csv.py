import pandas as pd
import os
import datetime
import tkinter as tk
from datetime import datetime, timedelta
from tkinter import *
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
filename = datetime.now()
print (filename)

open_file = filedialog.askopenfilename()
opened_file = open_file
df = opened_file
column_select = df['COLUMN NAME']
columns = df[column_select]
print(columns)

date = filename.strftime("%B_%d_%Y")
print(date)
for value in columns:
    df1 = df[df[column_select] == value]
    output_file_name = str(value) + "_" + date  + "roster" + "_" + ".xlsx"
    df1.to_excel(output_file_name, index=False)



