#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import string

m = 0
curFreq = 0;
bus_id = "random_id"

#Reducer reads from standard input which is the output from each mapper runing the Mapper1B.py script which outputs the highest visited business in each spilt
#i.e line = business_id, amount of ratings. It will output the highest visited business.
for line in sys.stdin:
    cur_id, freq = line.split(",")
    curFreq = int(freq)
    #checks for the biggest amount fo ratings
    #if the current amount is bigger than any previous amounts, replace the frequency number and bus_id    if curFreq>m:
        m= curFreq
        bus_id = cur_id

#write the business id along with its frequency into a output file
print "%s,%d" % (bus_id, m)
