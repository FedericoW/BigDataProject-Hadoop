#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import sys
import string

m = 0
curFreq = 0
bus_id = "random_id"

for line in sys.stdin:
    line = line.strip()
    cur_id, freq = line.split(",")
    curFreq = int(freq)
    if curFreq>m:
        m = curFreq
        bus_id = cur_id
      
print "%s,%d" % (bus_id, m)