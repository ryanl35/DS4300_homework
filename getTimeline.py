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
        followees = list(con.smembers(thisuser)) # list of users this person follows
        for user in followees:
            f = 'tweets:' + user.decode()
            tweets = con.zrange(f, 0, -1)    

    t1 = time.time()

    total = t1-t0
    print(total)

getTimeline()

