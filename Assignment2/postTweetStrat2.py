#!/usr/bin/python

import time
import redis
import csv

con = redis.Redis(host='localhost', port=6379, db = 0)

# Strategy 2, inserts tweet from CSV to Redis
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
        followers = list(con.smembers(user_id))
        j = 0
        for user in followers:
            actUser = user.decode()
            con.hset('timeline:'+ str(actUser), 'ts', ts)
            con.hset('timeline:'+ str(actUser), 'tweet', text)
            con.hset('timeline:'+ str(actUser), 'origin_id', user_id)
            j += 1
        if i % 1000 == 0: # keeps track of how far we are in the 1M tweet insertion
            print(i)
        i += 1

    t1 = time.time()

    total = t1-t0
    print(total)

postTweet()
