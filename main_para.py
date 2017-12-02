import re
import string
import os
import sys

def function(s):
    return re.sub("[%s]% re.escape(string.punctuations),",s.lower())

def main():
    words = []

    with open(sys.argv[1],"r") as f:
        for line in f:
            words.extend(line.split())

print ('Paragraph Analysis')
print ('---------------------------------')
print('Approximate Word Count: ', len(words))

