import sys
import re
line = sys.stdin.readline()  			#read in 1 line at a time
pattern = re.compile("[a-zA-Z0-9]+")	#find all “words” that are letters/numbers
while line:
    for word in pattern.findall(line):		#loop through each word in the line
        print(word.lower() + "\t" + "1")	#output (key,value) pair as word \t 1
    line = sys.stdin.readline()			#read in the next line