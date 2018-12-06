#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

current_word = None
current_count = 1

#Reducer reads each line from standard input. This input will be the intermediate key-value pairs
#provided by Mapper1A.py i.e line, 1 = business_id, stars, 1. Will output comma seperated values in the form: business_id,frequency
for line in sys.stdin:
    word, count = line.strip().split(',')
    #If current_word contains a value check
    if current_word:
        #if the business_id is equal to any previous current_word (previous business id), add one to frequency
        if word == current_word:
            current_count += int(count)
        #if not, a new business_id has been read, so print the business_id and it's frequency
        else:
            print "%s,%d" % (current_word, current_count)
            current_count = 1
    #Used to initialize the first business_id which serves as a starting point for comparing the next business_id
    current_word = word

if current_count > 1:
    print "%s,%d" % (current_word, current_count)
