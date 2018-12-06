#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

current_word = None
current_count = 1

for line in sys.stdin:
    word, count = line.strip().split(',')
    if current_word:
        if word == current_word:
            current_count += int(count)
        else:
            print "%s,%d" % (current_word, current_count)
            current_count = 1

    current_word = word

if current_count > 1:
    print "%s,%d" % (current_word, current_count)