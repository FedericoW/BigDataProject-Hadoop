#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import sys
import string

#Mapper reading each line from standard input
#Each line is a comma seperated value that has the form: business_id,stars
for line in sys.stdin:
    line = line.strip()
    #outputting a comma seperated value to standard output in the format: line, 1
    print "%s,%d" % (line, 1)
