import sys
current_word = None
current_count = 0
word = None
f = open('interm.txt', "r")
lines = list(f.readlines())
for line in lines: # sys.stdin:
    line = line.strip()
    try:
        word, count = line.split('\t', 1)
    except ValueError:
        continue
    
    count = int(count)
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
