#!/usr/bin/python

import time
import redis
import csv

con = redis.Redis(host='localhost', port=6379, db = 0)

# Strategy 2, retrieves all timelines from Redis
def getTimeline():
    t0 = time.time()
    for thisuser in range(15000):
        myFilter = "timeline:%d" % thisuser #filters for the set "timeline:userID"
        result = con.hgetall(myFilter)
    
    t1 = time.time()

    total = t1-t0
    print(total)

getTimeline()
