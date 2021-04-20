#!/usr/bin/env python
import csv
import re
from datetime import datetime

with open ('') as csv_file:
    r = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in r:
        if line_count == 0:
            columns = row
            #print(columns)

        else:
            pattern = re.compile('\d+\/\d+\/\d{4}')
            date = row[4]
            date = pattern.findall(date)[0]
            pattern = re.compile('(?<=\/)\d+(?=\/)')
            month = int(pattern.findall(date)[0])
            country = row[-1]

            amt = float(row[3]) * float(row[5])
            c_id = row[-2]
            print(str(month)+','+country+','+str(c_id)+':'+str(amt))
            
        line_count += 1

        if line_count > 5000:
            break