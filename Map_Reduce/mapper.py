import sys
import re
line = sys.stdin.readline()  			#read in 1 line at a time
pattern = re.compile(r'[^\s-]+')	#find all “words” that are letters/numbers
while line:
    for word in pattern.findall(line):		#loop through each word in the line
      pattern = re.compile("[aeiouyAEIOUY]+")
      vowels = pattern.findall(word)
      vowels = [i.lower() for i in vowels]
      if len(vowels) > 1:
        vowels = ''.join(sorted(vowels))
      elif len(vowels) > 0:
        vowels = sorted(vowels[0])
        vowels = ''.join(vowels)
      else:
        vowels = ''

      #for index,i in enumerate(vowels):
       #   print(str(index)+":",i)
      print(vowels + "\t" + "1")	#output (key,value) pair as word \t 1
            
    line = sys.stdin.readline()			#read in the next line
