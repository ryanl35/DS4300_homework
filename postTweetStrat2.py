#!/usr/bin/python

import time
import redis
import csv

con = redis.Redis(host='localhost', port=6379, db = 0)

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

        followees = list(con.smembers(user_id))
        j = 0
        for user in followees:
            con.hset('timeline: ' user, 'origin_id', user_id)
            con.hset('timeline: ' user, 'tweet', text)
            con.hset('timeline: ' user, 'ts', ts)
            j += 1
        i += 1

    t1 = time.time()

    total = t1-t0
    print(total)

postTweet()
