#!/usr/bin/python

import time
import redis
import csv

con = redis.Redis(host='localhost', port=6379, db = 0)

# Strategy 1, inserts tweets from csv to Redis
def postTweet():
    tweetscsv = open("generatedTweets.csv", "r") #opens tweets csv from HW1
    cleanedTweets = csv.reader(tweetscsv, delimiter=',')
    next(cleanedTweets) #skips the first row
    i = 0 
    dict = {}
    t0 = time.time()
    for tweet in cleanedTweets:
        user_id = tweet[1] 
        text = tweet[3]
        ts = time.time()
        con.zadd('tweets:' + str(user_id), {text:ts})
        i += 1

    t1 = time.time()

    total = t1-t0
    print(total)

postTweet()

