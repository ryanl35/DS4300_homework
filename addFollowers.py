#!/usr/bin/python

import time
import redis
import csv

con = redis.Redis(host='localhost', port=6379, db = 0)

# Strategy 1, Run first, Adds Following ID's to user ID
def addFollowers():
    followerscsv = open("generatedFollowers.csv", "r") #opens followers csv from HW1
    cleanedFollowers = csv.reader(followerscsv, delimiter=',')
    next(cleanedFollowers) #skips the first row
    i = 0 
    dict = {}
    t0 = time.time()
    for follower in cleanedFollowers:
        user_id = follower[0]
        follows_id = follower[1]
        con.sadd(user_id, follows_id)
        i += 1

    t1 = time.time()

    total = t1-t0
    print(total)

addFollowers()

