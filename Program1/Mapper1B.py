#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import sys
import string

#Mapper reads from standard input which is the output from Reducer1A.py which is a comma seperated values
#i.e line = business_id, amount of ratings. It will output the highest visited business_id along with the amount of times rated.
m = 0
curFreq = 0
bus_id = "random_id"

for line in sys.stdin:
    line = line.strip()
    cur_id, freq = line.split(",")
    curFreq = int(freq)
    #checks for the biggest amount fo ratings
    #if the current amount is bigger than any previous amounts, replace the frequency number and bus_id
    if curFreq>m:
        m = curFreq
        bus_id = cur_id

#Output comma seperated value in the format: business_id,frequency
print "%s,%d" % (bus_id, m)
