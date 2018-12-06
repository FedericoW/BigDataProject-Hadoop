#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import sys
import string

for line in sys.stdin:
    line = line.strip()
    print "%s,%d" % (line, 1)
