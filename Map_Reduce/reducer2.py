#!/usr/bin/env python
import sys

current_combo = None
current_month = None
current_country = None
current_id = None
current_total = 0
current_high = 0
high_month = None
high_country = None
high_id = None
month = None
country = None
id = None
amt = None

word = None
f = open('sorted.txt', "r")
lines = list(f.readlines())
for line in lines: # for line in sys.stdin:
    line = line.strip()
    line = line.split(":")
    items = [i for i in line[0].split(',')]
    kv = [items,line[1]]

    month = kv[0][0]
    country = kv[0][1]
    id = kv[0][2]
    amt = kv[1]

    # if same country,month
    if current_month == month and current_country == country:
        # if same id
        if current_id == id:
            current_total += float(amt)
            if current_total > current_high:
                current_high = current_total
                high_month = month
                high_country = country
                high_id = id
        
        # if different id
        else:
            current_id = id 
            current_total = 0

    # if same month, different country
    elif current_month == month and current_country != country:
        print('%s,%s:%s' % (high_month, current_country, high_id))

        current_country = country
        current_id = id
    
    # if different country,month
    else:
        print('%s,%s:%s' % (high_month, high_country, high_id))
        current_month = month
        current_country = country
        current_id = id


#if current_word == word:
 #   print('%s\t%s' % (current_word, current_count))