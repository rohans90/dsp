    
import numpy as np
import csv as csv
import pandas as pd

readdata = csv.reader(open('/Users/Rohan/Desktop/football.csv', 'r'))
data = []
for row in readdata:
    data.append(row)
Header = data[0]
    
for row in data[1:]:
    cal =  int(row[5]) - int(row[6])
    print (cal)

###Aston Villa

