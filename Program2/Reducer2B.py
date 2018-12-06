# Reducer 2B 

import sys
import string
import heapq

heap = []

#Reducer reads from standard input which is the output from each mapper runing the Mapper2B.py script which outputs the top ten rated businesses
#i.e line = average star rating, business_id. It will output the top 10 business_ids along with their avg_rating.
#The top 10 businesses are selected according to their avg_rating.
for line in sys.stdin:
    line  = line.strip()
	
	#Storing the business_id and its average rating into a tuple
    freq, cur_id = line.split(",")
    tup = float(freq), cur_id
    
	#If the heap does not yet have 10 tuples then just push each subsequent tuple
    if len(heap) < 10:
      heapq.heappush(heap, tup)
	#else pop a tuple and push a new one so that the top ten rated businesses are always stored
    else:
      heapq.heappushpop(heap, tup)

heap = sorted(heap, reverse=True)

#Output comma seperated value in the format: avg_rating,business_id
for tup in heap:
    b_tup = tup[0], tup[1].strip("\n")
    print "%.2f,%s" % (tup[0], tup[1])