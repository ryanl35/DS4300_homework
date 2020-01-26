#!/usr/bin/python

import time
import redis
import csv

con = redis.Redis(host='localhost', port=6379, db = 0)

def getTimeline():
    t0 = time.time()
    for x in range(15000):
        i = 0 
        thisuser = x
        followees = list(con.smembers(thisuser))
        for user in followees:
            f = 'tweets:' + user.decode()
            tweets = con.zrange(f, 0, -1)
            j = 0 
            for tweet in tweets:
                j += 1
            i += 1
    

    t1 = time.time()

    total = t1-t0
    print(total)

getTimeline()

