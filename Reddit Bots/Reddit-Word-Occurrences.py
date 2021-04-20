# Reddit bot to count the occurences of a word or phrase, every 10 minutes #

''' Imports '''
import praw
import re
import time

''' Functions '''
def getWordCount(count):
    previous_count = count
    ten = False
    t1 = time.time()
    
    while ten is False:
        for comment in subreddit.stream.comments():
            try:
                file = open(r"")
            except:
                file = open(r"")
            # Check if 10 minutes has passed
            t2 = time.time()
            if t2 - t1 >= 600:
                ten = True
                file.write("{} \n".format(time.strftime("%H:%M:%S")))
                file.close()
                break

            # Search for word
            if re.search(r"[Tt][Rr][Uu][Mm][Pp]", comment.body) is not None:
                count = count + 1
                try:
                    print(count)
                    
                except:
                    print('didn\'t work')
                print("\n====================================\n")
    change = count - previous_count
    return count, change


''' Main '''
# reddit api login
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')


# subreddit scope
subreddit = reddit.subreddit('all')


# Every 10 minutes log count and calculate the change in count
try:
    file = open(r"")
except:
    file = open(r"C")

file.write("# {}".format(time.strftime("%A")))
file.write(" \n")
file.write("# {}".format(time.strftime("%m %d %y")))
file.write(" \n")
file.write("# {}".format(time.strftime("%H:%M:%S")))
file.write(" \n\n")

current_count = 0
while True:
    current_count, change_in_count = getWordCount(current_count)

    try:
        file = open(r"")
    except:
        file = open(r"")
    file.write("Count: {} \nChange: {}\n\n".format(current_count,change_in_count))
    print("Count:",current_count,"\nChange:",change_in_count)

file.close()

                
