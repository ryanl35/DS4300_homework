#!/usr/bin/python

import time
import redis
import csv

con = redis.Redis(host='localhost', port=6379, db = 0)

def postTweet():
    with open("generatedTweets.csv", "r") as tweetscsv: #opens tweets csv from HW1
        cleanedTweets = csv.reader(tweetscsv, delimiter=',')
        next(cleanedTweets) #skips the first row
        i = 0 
        dict = {}
        for tweet in cleanedTweets:
            index = i
            text = tweet[3]
            dict = {text:index}
            con.zadd('tweets',dict)
            i += 1

postTweet()
