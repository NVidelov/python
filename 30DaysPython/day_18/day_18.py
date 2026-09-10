# Day 18 - 30 Days of Python Challenge

# RegEx

import re
from collections import Counter

'''
re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string
'''

# Exercise Level 1

# 1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
regex_pattern = r'[A-Za-z]+'
matches = re.findall(regex_pattern, paragraph)
word_count = Counter(matches)

result = [(count, word) for word, count in word_count.most_common()]
print(result)

# 2
