#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import sys


current_bus_id = None
current_count = 1
stars_total = 0

#Reducer reads each line from standard input. This input will be the intermediate key-value pairs
#provided by Mapper2A.py i.e line, 1 = business_id, stars, 1. Will output comma seperated values in the form: business_id,avg_rating
for line in sys.stdin:
    bus_id, stars, count = line.strip().split(',')
	#Skipping over the column headers 
    if stars is "stars":
        continue
    #If current_bus_id contains a value check if the business_id is equal to the previous current_bus_id/previous business id
    if current_bus_id:
		#If true then accumulate the number of occurence of that business id, as well as the star rating
        if bus_id == current_bus_id:
            current_count += int(count)
            stars_total += float(stars)
        else:
		#If not then a new business_id has been read, so print the business_id and it's average rating.
		#Set new business_id to compare with
            print "%s,%.2f" % (current_bus_id, (stars_total/current_count))
            current_count = 1
	        current_bus_id = bus_id
            stars_total = float(stars)
    #Used to initialize the first business_id which serves as a starting point for comparing the next business_id
    else:
        current_bus_id = bus_id
        stars_total = float(stars)

if current_count > 1:
    print "%s,%.2f" % (current_bus_id, (stars_total/current_count))
